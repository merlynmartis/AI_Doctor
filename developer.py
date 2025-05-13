def render_developer():
    import streamlit as st
    from PIL import Image

    st.markdown("""
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
        }

        .dev-text-wrapper {
            display: flex;
            flex-direction: column;
            justify-content: center;
            height: 100%;
        }

        .dev-text {
            color: #002B5B;
            font-weight: bold;
            font-size: 22px;
        }

        .social-icons a {
            margin-right: 15px;
            text-decoration: none;
            font-size: 24px;
        }

        .title {
            color: #002B5B;
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 30px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>Meet the Developer</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        image = Image.open("images/me.jpg")
        st.image(image, width=390)  # Adjust width as needed

    with col2:
        st.markdown("""
            <div class="dev-text-wrapper">
                <div class="dev-text">
                    <p><b>Merlyn Joselin Martis</b><br>
                    <b>Email:</b> merlynmartis714@gmail.com<br>
                    <b>Phone:</b> +91 9845234265<br>
                    <b>Location:</b> Mangaluru, Karnataka, India</p>
                    <div class="social-icons">
                        <a href="https://www.instagram.com/merlyn.martis" target="_blank"><i class="fab fa-instagram"></i></a>
                        <a href="https://www.linkedin.com/in/merlynmartis14" target="_blank"><i class="fab fa-linkedin"></i></a>
                        <a href="https://github.com/merlynmartis" target="_blank"><i class="fab fa-github"></i></a>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
