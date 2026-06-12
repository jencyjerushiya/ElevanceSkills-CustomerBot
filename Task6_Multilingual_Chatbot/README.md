# Multilingual Chatbot

## Project Overview

The Multilingual Chatbot is an AI-powered application developed using Python and Streamlit that automatically detects the language of user input and translates it into English. The chatbot demonstrates multilingual interaction by supporting multiple languages while providing a simple and intuitive user interface.

## Features

* Automatic language detection.
* Translation of user input into English.
* Supports multiple languages, including:

  * English
  * French
  * Spanish
  * German
* Displays the detected language in a user-friendly format.
* Interactive web interface built with Streamlit.

## Technologies Used

* Python
* Streamlit
* langdetect
* deep-translator

## Project Structure

```text
Task6_Multilingual_Chatbot/
│── app.py
│── README.md
│── Task6_Internship_Report.docx
```

## How to Run the Project

1. Install the required libraries:

```bash
pip install streamlit langdetect deep-translator
```

2. Open a terminal in the project folder.

3. Run the application:

```bash
streamlit run app.py
```

4. Open the local URL displayed in your browser.

5. Enter text in any supported language and click **Process**.

## Example Inputs

* English: `Hello, how are you?`
* French: `Bonjour, comment allez-vous ?`
* Spanish: `Hola, ¿cómo estás?`
* German: `Guten Morgen`

## Expected Output

The chatbot:

* Detects the language of the input text.
* Displays the detected language name.
* Translates the text into English.
* Presents the translated result through a simple Streamlit interface.

## Disclaimer

This project is intended for educational purposes as part of an AI & Data Science internship and demonstrates multilingual language detection and translation techniques.

## Author

Jency Jerushiya J

