import streamlit as st
from chatbot import get_answer

st.set_page_config(
    page_title="Domain Expert Chatbot",
    page_icon="🤖"
)

st.title("🤖 Domain Expert Chatbot")
st.write(
    "Ask questions about Artificial Intelligence, Machine Learning, "
    "Deep Learning, NLP, Computer Vision, and related topics."
)

user_query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_query.strip():
        answer = get_answer(user_query)

        st.subheader("Response")
        st.write(answer)
    else:
        st.warning("Please enter a question.")