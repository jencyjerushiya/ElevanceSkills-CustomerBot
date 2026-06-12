# Dynamic Knowledge Base Chatbot

## Project Overview

The Dynamic Knowledge Base Chatbot is an AI-powered application developed using Python, Sentence Transformers, and Streamlit. It retrieves relevant information from a knowledge base and demonstrates dynamic expansion by automatically incorporating newly added content without requiring changes to the chatbot logic.

The project showcases semantic search techniques and a simple mechanism for updating the chatbot's knowledge over time.

---

## Features

* Retrieves relevant information using semantic similarity search.
* Dynamically loads the latest content from the knowledge base.
* Automatically reflects newly added information without modifying the source code.
* Provides a simple and interactive user interface using Streamlit.
* Demonstrates the concept of a dynamically expandable knowledge repository.

---

## Technologies Used

* Python
* Streamlit
* Sentence Transformers
* Natural Language Processing (NLP)

---

## Project Structure

```text
Task1_Dynamic_Knowledge_Base/
│── app.py
│── chatbot.py
│── knowledge_base.txt
│── README.md
│── Task1_Internship_Report.docx
```

---

## How to Run the Project

1. Install the required dependencies:

```bash
pip install streamlit sentence-transformers
```

2. Open a terminal in the project folder.

3. Run the application:

```bash
streamlit run app.py
```

4. Open the local URL displayed in your browser.

5. Enter a query to retrieve information from the knowledge base.

---

## Dynamic Update Demonstration

1. Open `knowledge_base.txt`.
2. Add a new piece of information and save the file.
3. Run a related query in the chatbot.
4. The chatbot will retrieve the newly added information without requiring changes to the application code.

---

## Disclaimer

This project is developed for educational purposes as part of an AI & Data Science internship and demonstrates semantic retrieval with a dynamically updatable knowledge base.

---

## Author

Jency Jerushiya J

