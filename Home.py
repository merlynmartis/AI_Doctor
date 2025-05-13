import streamlit as st
import numpy as np
import pandas as pd
import pickle
import ast
import base64

from about import render_about
from contact import render_contact
from developer import render_developer

# ----------- Page Config ----------- #
st.set_page_config(
    page_title="AI Doctor",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------- Background Image Encoding ----------- #
def get_base64_of_bin_file(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img_base64 = get_base64_of_bin_file("images/background.png")

st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)), 
                    url("data:image/png;base64,{bg_img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #002B5B; /* Dark blue font */
    }}

    html, body {{
        color: #002B5B;
    }}

    * {{
        color: #002B5B !important;  /* Force all elements to inherit dark blue text */
    }}

    .main > div {{
        background-color: rgba(255, 255, 255, 0.6);
        padding: 2rem;
        border-radius: 10px;
    }}

    .stTabs [data-baseweb="tab-list"] {{
        justify-content: center;
    }}
    .stTabs [data-baseweb="tab-list"] button {{
        margin: 0 20px !important;
    }}
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {{
        font-size: 20px !important;
        font-weight: bold !important;
        color: #002B5B !important;

    }}
    </style>
""", unsafe_allow_html=True)


# ----------- Load Data & Model ----------- #
sym_des = pd.read_csv("datasets/symptoms_df.csv")
precautions_df = pd.read_csv("datasets/precautions_df.csv")
workout_df = pd.read_csv("datasets/workout_df.csv")
description = pd.read_csv("datasets/description.csv")
medications_df = pd.read_csv('datasets/medications.csv')
diets_df = pd.read_csv("datasets/diets.csv")

@st.cache_resource
def load_model():
    return pickle.load(open('models/svc.pkl', 'rb'))

svc = load_model()

# ----------- Utility Functions ----------- #
def safe_join(items):
    if isinstance(items, list):
        return ', '.join(str(i).strip() for i in items if pd.notnull(i))
    return str(items)

def helper(dis):
    desc = " ".join(description[description['Disease'] == dis]['Description'].values)
    pre = precautions_df[precautions_df['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.tolist()
    med_raw = medications_df[medications_df['Disease'] == dis]['Medication'].tolist()
    med = ast.literal_eval(med_raw[0]) if med_raw and isinstance(med_raw[0], str) and med_raw[0].startswith("[") else med_raw
    diet_raw = diets_df[diets_df['Disease'] == dis]['Diet'].tolist()
    die = ast.literal_eval(diet_raw[0]) if diet_raw and isinstance(diet_raw[0], str) and diet_raw[0].startswith("[") else diet_raw
    wrkout = workout_df[workout_df['disease'] == dis]['workout'].tolist()
    return desc, pre, med, die, wrkout

# Symptom dictionary and diseases mapping
symptoms_dict = {
    'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3,
    'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8,
    'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12,
    'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16,
    'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20,
    'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24,
    'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28,
    'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32,
    'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36,
    'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40,
    'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44,
    'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47,
    'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50,
    'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53,
    'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57,
    'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60,
    'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64,
    'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69,
    'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72,
    'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75,
    'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78,
    'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82,
    'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85,
    'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88,
    'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91,
    'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94,
    'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98,
    'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101,
    'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104,
    'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108,
    'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111,
    'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114,
    'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116,
    'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119,
    'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122,
    'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126,
    'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129,
    'red_sore_around_nose': 130, 'yellow_crust_ooze': 131
}

diseases_list = {
    0: '(vertigo) Paroymsal  Positional Vertigo', 1: 'AIDS', 2: 'Acne',
    3: 'Alcoholic hepatitis', 4: 'Allergy', 5: 'Arthritis',
    6: 'Bronchial Asthma', 7: 'Cervical spondylosis', 8: 'Chicken pox',
    9: 'Chronic cholestasis', 10: 'Common Cold', 11: 'Dengue',
    12: 'Diabetes ', 13: 'Dimorphic hemmorhoids(piles)', 14: 'Drug Reaction',
    15: 'Fungal infection', 16: 'GERD', 17: 'Gastroenteritis',
    18: 'Heart attack', 19: 'Hepatitis B', 20: 'Hepatitis C',
    21: 'Hepatitis D', 22: 'Hepatitis E', 23: 'Hypertension ',
    24: 'Hyperthyroidism', 25: 'Hypoglycemia', 26: 'Hypothyroidism',
    27: 'Impetigo', 28: 'Jaundice', 29: 'Malaria', 30: 'Migraine',
    31: 'Osteoarthristis', 32: 'Paralysis (brain hemorrhage)',
    33: 'Peptic ulcer diseae', 34: 'Pneumonia', 35: 'Psoriasis',
    36: 'Tuberculosis', 37: 'Typhoid', 38: 'Urinary tract infection',
    39: 'Varicose veins', 40: 'hepatitis A'
}


def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in patient_symptoms:
        if item in symptoms_dict:
            input_vector[symptoms_dict[item]] = 1
        else:
            st.error(f"Unknown symptom: {item}")
            st.stop()
    prediction = svc.predict([input_vector])[0]
    return diseases_list[prediction]

# ----------- Tabs Layout ----------- #
tab1, tab2, tab3, tab4 = st.tabs(["Home", "About", "Contact", "Developer"])

# ----------- Home Tab ----------- #
with tab1:
    st.markdown("""
        <div style='text-align: center;'>
            <h1 style='font-size: 90px; margin-bottom: 10px; font-weight: bold;'>AI Doctor</h1>
            <h3 style='color: #003366; font-style: italic; font-size: 19px; margin-top: 0;'>
                <strong>Your Pocket Doctor - Smarter and Faster</strong>
            </h3>
            <p style='font-size:20px; font-weight:700;'><strong>Select your symptoms and get a possible diagnosis with treatment recommendations.</strong></p>
            <p style='font-size:20px; font-weight:700;'><strong>Choose your symptoms</strong></p>
        </div>
    """, unsafe_allow_html=True)

    user_symptoms = st.multiselect("", options=list(symptoms_dict.keys()))

    st.markdown("""
        <style>
        .stMultiSelect div[role="listbox"] > div {
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
        }

        .stMultiSelect div[data-baseweb="tag"] {
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
        }

        .stButton button {
            font-size: 20px;
            padding: 10px 30px;
            border-radius: 8px;
            border: 1px solid #8fadcf;
            color: #8fadcf;
            background-color: lightblue;
            margin-top: 10px;
        }

        /* Change selected symptom tags to blue */
        [data-baseweb="tag"] {
            background-color: #8fadcf !important;
            color: white !important;
            border: none !important;
        }

        [data-baseweb="tag"]:hover {
            background-color: #8fadcf !important;
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("Analyze Symptoms"):
        if not user_symptoms:
            st.error("Please select at least one symptom.")
        else:
            predicted_disease = get_predicted_value(user_symptoms)
            dis_des, precautions, medications, rec_diet, workout = helper(predicted_disease)

            st.success(f"Predicted Disease: **{predicted_disease}**")
            # Modal-like sections for all information
            with st.expander("View Description"):
                st.markdown(f"<p style='font-size:20px;'><b>Description:</b> {dis_des}</p>", unsafe_allow_html=True)
            with st.expander("View Precautions"):
                st.markdown(f"<p style='font-size:20px;'><b>Precautions:</b> {safe_join(precautions[0])}</p>", unsafe_allow_html=True)

            with st.expander("View Medications"):
                st.markdown(f"<p style='font-size:20px;'><b>Medication:</b> {safe_join(medications)}</p>", unsafe_allow_html=True)

            with st.expander("View Recommended Diet"):
                st.markdown(f"<p style='font-size:20px;'><b>Recommended Diet:</b> {safe_join(rec_diet)}</p>", unsafe_allow_html=True)

            with st.expander("View Workouts"):
                st.markdown(f"<p style='font-size:20px;'><b>Workouts:</b> {safe_join(workout)}</p>", unsafe_allow_html=True)

# ----------- Other Tabs ----------- #
with tab2:
    render_about()

with tab3:
    render_contact()

with tab4:
    render_developer()
