import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍"
)

st.title("🌍 AI Language Translation Tool")
st.write("Translate text between multiple languages.")

text = st.text_area("Enter Text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Tamil": "ta",
    "Telugu": "te",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

source_lang = st.selectbox(
    "Source Language",
    list(languages.keys())
)

target_lang = st.selectbox(
    "Target Language",
    list(languages.keys())
)

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter text.")
    else:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Successful")

        st.text_area(
            "Translated Text",
            translated,
            height=120
        )