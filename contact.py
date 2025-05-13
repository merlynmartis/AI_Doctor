def render_contact():
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
    <div style='color:#002B5B; font-weight:bold; font-size:22px;'>

    <center>If you have questions or feedback, feel free to reach out:

    📧 Email: merlynmartis714@gmail.com  
    📍 Address: Mangalore, India  
    📱Phone: +91 9845234265
    </center>
    </div>
    """, unsafe_allow_html=True)
