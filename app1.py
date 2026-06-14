import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ data
faq = pd.read_csv("faq.csv")

questions = faq["Question"]
answers = faq["Answer"]

# Convert questions to s
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

st.title("🤖 FAQ Chatbot")

user_question = st.text_input("Ask a question:")

if st.button("Get Answer"):

    if user_question.strip() != "":

        user_vector = vectorizer.transform([user_question])

        similarity = cosine_similarity(
            user_vector,
            question_vectors
        )

        best_match = similarity.argmax()

        st.success(answers[best_match])