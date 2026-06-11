# Task 5 - Customer Sentiment Analysis Chatbot

## Project Overview

This project is a Customer Sentiment Analysis Chatbot developed using Python, TextBlob, and Streamlit. It analyzes customer messages to identify whether the sentiment is **Positive**, **Negative**, or **Neutral**, and generates an appropriate response based on the detected emotion.

The chatbot demonstrates the practical application of Natural Language Processing (NLP) techniques for understanding customer feedback and improving user interactions.

---

## Features

* Detects customer sentiment as:

  * Positive
  * Negative
  * Neutral
* Generates appropriate responses based on the detected sentiment.
* Displays a sentiment (polarity) score for each message.
* Provides an interactive and user-friendly web interface using Streamlit.
* Supports real-time analysis of user-entered text.

---

## Technologies Used

* Python
* Streamlit
* TextBlob
* Natural Language Processing (NLP)

---

## Project Structure

```text
Task5_Sentiment_Analysis/
│── app.py
│── sentiment_chatbot.py
│── README.md
│── Task5_Internship_Report.docx
```

---

## How to Run the Project

1. Install the required dependencies:

```bash
pip install streamlit textblob
```

2. Open a terminal in the project folder.

3. Run the application:

```bash
streamlit run app.py
```

4. Open the local URL displayed in your browser.

5. Enter a customer message and click **Analyze Sentiment** to view the results.

---

## Example Test Cases

| Input                                               | Expected Sentiment |
| --------------------------------------------------- | ------------------ |
| I am extremely happy with your customer support.    | Positive           |
| I am disappointed with the quality of your service. | Negative           |
| The meeting starts at 10 AM.                        | Neutral            |

---

## Expected Output

The chatbot:

* Identifies the sentiment of the user's message.
* Displays the detected sentiment category.
* Shows the sentiment polarity score.
* Generates an appropriate customer-focused response.

---

## Disclaimer

This project is intended for educational and learning purposes as part of an AI & Data Science internship. It demonstrates sentiment analysis techniques and should not be considered a replacement for professional customer support systems.

---

## Author

Jency Jerushiya J

