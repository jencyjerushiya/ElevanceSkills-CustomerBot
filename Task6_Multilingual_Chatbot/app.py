import streamlit as st
from langdetect import detect
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Multilingual Chatbot",
    page_icon="🌍"
)

st.title("🌍 Multilingual Chatbot")

st.write(
    "This chatbot automatically detects the language of your message "
    "and translates it into English."
)

# Dictionary to convert language codes to full names
language_names = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "hi": "Hindi",
    "ta": "Tamil",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese (Simplified)"
}

user_input = st.text_area("Enter your message:")

if st.button("Process"):

    if user_input.strip():

        try:
            # Detect language
            detected_language = detect(user_input)

            # Translate to English
            translated_text = GoogleTranslator(
                source="auto",
                target="en"
            ).translate(user_input)

            # Display results
            st.subheader("Detected Language")
            st.write(
                language_names.get(
                    detected_language,
                    detected_language
                )
            )

            st.subheader("Translated to English")
            st.write(translated_text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter some text.")