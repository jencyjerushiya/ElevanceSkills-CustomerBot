import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Dynamic Knowledge Base Chatbot",
    page_icon="📚"
)

st.title("📚 Dynamic Knowledge Base Chatbot")

st.write(
    "This chatbot retrieves information from a dynamically updatable knowledge base."
)

user_query = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if user_query.strip():
        answer = get_response(user_query)

        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")