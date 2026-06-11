import streamlit as st
from sentiment_chatbot import analyze_sentiment

st.set_page_config(
    page_title="Customer Sentiment Analysis Chatbot",
    page_icon="💬"
)

st.title("💬 Customer Sentiment Analysis Chatbot")

st.write(
    """
This chatbot analyzes customer messages and identifies whether the sentiment is
**Positive, Negative, or Neutral**, then provides an appropriate response.
"""
)

user_input = st.text_area(
    "Enter your message:",
    placeholder="Example: I am very happy with your service!"
)

if st.button("Analyze Sentiment"):

    if user_input.strip():

        sentiment, score, response = analyze_sentiment(user_input)

        st.success("Analysis Complete")

        st.subheader("Detected Sentiment")
        st.write(sentiment)

        st.subheader("Sentiment Score")
        st.write(f"{score:.2f}")

        st.subheader("Chatbot Response")
        st.write(response)

    else:
        st.warning("Please enter a message before clicking Analyze Sentiment.")

st.markdown("---")
st.caption(
    "This project was developed for educational purposes as part of an AI & Data Science Internship."
)