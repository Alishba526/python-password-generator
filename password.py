import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.set_page_config(
        page_title="🔒 Password Generator",
        page_icon="🔒",
        layout="centered",
    )

    st.markdown(
        """
        <style>
        /* Background image */
        .stApp {
            background-image: url("https://img.freepik.com/free-photo/abstract-oil-bubbles-background_23-2148205128.jpg?t=st=1741535235~exp=1741538835~hmac=8f0e666d5200d9bd2b8276b8e9d91167343c1e3d98b5147d3c2d1a56a375c01e&w=1380");
            background-size: cover;
            background-position: center;
        }

        /* Transparent container for content */
        .stContainer {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        /* Button styling */
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #45a049;
        }

        /* Header styling */
        .stMarkdown h1 {
            color: #4CAF50;
            text-align: center;
        }
        .stMarkdown h2 {
            color: #FF5733;
        }
        .stMarkdown h3 {
            color: #33A8FF;
        }
        .stMarkdown p {
            color: #555555;
        }

        /* Code block styling */
        .stCodeBlock {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.title("🔒 Beautiful Password Generator")
        st.write("Generate strong and secure passwords with ease!")

        with st.sidebar:
            st.header("⚙️ Settings")
            length = st.slider("Password Length", min_value=8, max_value=32, value=12)
            use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
            use_digits = st.checkbox("Include Digits", value=True)
            use_special_chars = st.checkbox("Include Special Characters", value=True)

        if st.button("Generate Password"):
            password = generate_password(length, use_uppercase, use_digits, use_special_chars)
            st.success("🎉 Your generated password is:")
            st.code(password, language="plaintext")

            if st.button("📋 Copy to Clipboard"):
                st.write("✅ Password copied to clipboard!")
                st.experimental_set_query_params(password=password)

        # Footer
        st.markdown("---")
        st.markdown("Made ❤️ by [alishba rehman]")

if __name__ == "__main__":
    main()

