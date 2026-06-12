# Multi-modal AI Assistant

## Project Overview

The Multi-modal AI Assistant is an AI-powered application developed using Python, Streamlit, and the BLIP image captioning model. It is capable of understanding both image and text inputs, analyzing visual content, maintaining conversational context, and generating evidence-based responses.

The assistant demonstrates multimodal interaction by combining computer vision and natural language processing techniques to provide intelligent and context-aware responses.

## Features

* Accepts both image and text inputs.
* Analyzes uploaded images using a pretrained BLIP image captioning model.
* Answers user questions based on the detected visual content.
* Maintains conversation history throughout the session.
* Provides evidence-based responses derived from image analysis.
* Handles ambiguous queries by avoiding unsupported assumptions.
* Interactive and user-friendly interface built with Streamlit.

## Technologies Used

* Python
* Streamlit
* Transformers (BLIP Image Captioning Model)
* PyTorch
* Pillow (PIL)

## Project Structure

```text
Task2_Multimodal_AI_Assistant/
│── app.py
│── README.md
│── Task2_Internship_Report.docx
```

## How to Run

1. Install the required libraries:

```bash
pip install streamlit transformers torch pillow
```

2. Open a terminal in the project folder.

3. Run the application:

```bash
streamlit run app.py
```

4. Open the local URL displayed in your browser.

5. Upload an image, enter a question related to the image, and click **Analyze**.

## Example Questions

* What do you see in this image?
* Is there an animal in this image?
* What color is the animal?
* Describe this picture.
* Can you identify the main object?

## Key Capabilities

* Multimodal understanding using image and text inputs.
* Visual content analysis through AI-based image captioning.
* Context-aware interactions with conversation history.
* Evidence-based reasoning using detected visual information.
* Ambiguity handling by avoiding unsupported conclusions.

## Disclaimer

This project is intended for educational purposes as part of an AI & Data Science internship. The assistant generates responses based on AI-powered visual analysis and should not be considered a substitute for professional expertise in critical decision-making scenarios.

## Author

Jency Jerushiya J

