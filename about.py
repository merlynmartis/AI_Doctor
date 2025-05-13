def render_about():
    import streamlit as st

    # Custom CSS for Roboto font and 20px size
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Roboto', sans-serif;
            font-size: 20px;
        }

        h1 {
            font-size: 28px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Page Content
    st.markdown("""
    <div style='color:#002B5B; font-weight:bold; font-size:20px;'>

    <b>AI Doctor is a smart healthcare assistant that uses advanced machine learning to help users understand and respond to their health concerns more effectively. With a powerful backend of multiple ML models and Flask-based deployment, it delivers quick and accurate disease predictions based on user symptoms.

    <b>Once a condition is identified, AI Doctor provides:

    <ul>
      <li><b>Detailed disease descriptions</b> for user awareness</li>
      <li><b>Preventive advice</b> to avoid complications and manage the condition</li>
      <li><b>Non-prescriptive medication suggestions</b> for informational purposes</li>
      <li><b>Workout tips</b> aligned with the condition to support physical health</li>
      <li><b>Dietary guidance</b> for recovery and long-term wellness</li>
    </ul>

    <b>AI Doctor is designed to <b>empower users</b> by delivering accessible, trustworthy, and personalized health information. While it’s not a replacement for professional medical care, it serves as a reliable tool for initial self-assessment.</b>

    Whether you're dealing with symptoms or simply exploring your health, <b>AI Doctor offers a private, always-available solution</b> that encourages proactive and informed health management—anytime, anywhere.</b>

    </div>
    """, unsafe_allow_html=True)
