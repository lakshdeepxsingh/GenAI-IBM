import streamlit as st
import pickle

import os
import pickle
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(current_dir, "fake_news_model.pkl")
vectorizer_path = os.path.join(current_dir, "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

# Page Title
st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detector")
st.write("Enter a news article below and click **Detect**.")

# User Input
news = st.text_area("Paste News Article Here")

# Prediction
if st.button("Detect"):

    if news.strip() == "":
        st.warning("Please enter some news text.")
    else:

        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)

        if prediction[0] == "FAKE":
            st.error("🚨 This news appears to be FAKE.")
        else:
            st.success("✅ This news appears to be REAL.")