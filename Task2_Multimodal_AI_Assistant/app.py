import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# -----------------------------
# Load BLIP model only once
# -----------------------------
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )
    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )
    return processor, model

processor, model = load_model()

# -----------------------------
# Streamlit Page
# -----------------------------
st.set_page_config(
    page_title="🤖 Multi-modal AI Assistant",
    page_icon="🤖"
)

st.title("🤖 Multi-modal AI Assistant")

st.write(
    """
Upload an image and ask questions about it.

The assistant:
- Analyzes visual content
- Maintains conversation history
- Provides evidence-based responses
- Handles ambiguous questions carefully
"""
)

# -----------------------------
# Session Memory
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "caption" not in st.session_state:
    st.session_state.caption = ""

# -----------------------------
# Upload Image
# -----------------------------
uploaded_image = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

question = st.text_input(
    "Ask something about the image:"
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("Analyze"):

    if uploaded_image is None:
        st.warning("Please upload an image first.")

    elif question.strip() == "":
        st.warning("Please enter a question.")

    else:

        image = Image.open(uploaded_image).convert("RGB")
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Generate caption once
        if st.session_state.caption == "":
            inputs = processor(images=image, return_tensors="pt")
            output = model.generate(**inputs)

            st.session_state.caption = processor.decode(
                output[0],
                skip_special_tokens=True
            )

        caption = st.session_state.caption.lower()
        user_question = question.lower()

        # -----------------------------
        # Reasoning Layer
        # -----------------------------

        # 1. Description
        if "describe" in user_question or "what do you see" in user_question:

            response = (
                f"Based on my visual analysis, the image appears to show:\n\n"
                f"**{st.session_state.caption}**\n\n"
                "This response is generated from the detected visual content."
            )

        # 2. Color questions
        elif "color" in user_question or "colour" in user_question:

            colors = [
                "orange",
                "black",
                "white",
                "brown",
                "gray",
                "grey",
                "blue",
                "green",
                "yellow",
                "red",
                "pink"
            ]

            detected = None

            for c in colors:
                if c in caption:
                    detected = c
                    break

            if detected:
                response = (
                    f"Based on the detected visual description, "
                    f"the primary visible color appears to be **{detected}**."
                )
            else:
                response = (
                    "I cannot determine the color confidently from the "
                    "available visual evidence."
                )

        # 3. Animal questions
        elif "animal" in user_question:

            animals = [
                "kitten",
                "cat",
                "dog",
                "bird",
                "horse",
                "cow",
                "lion",
                "tiger",
                "bear",
                "elephant"
            ]

            found = None

            for a in animals:
                if a in caption:
                    found = a
                    break

            if found:
                response = (
                    f"Yes. Based on the detected visual evidence, "
                    f"the image appears to contain a **{found}**."
                )
            else:
                response = (
                    "I cannot confidently identify an animal "
                    "from the uploaded image."
                )

        # 4. Ownership / impossible questions
        elif "owner" in user_question or "whose" in user_question:

            response = (
                "The owner or identity of individuals or animals "
                "cannot be determined from this image alone."
            )

        # 5. Default intelligent response
        else:

            response = (
                f"My visual analysis suggests the image contains:\n\n"
                f"**{st.session_state.caption}**\n\n"
                "However, I cannot answer your specific question "
                "with high confidence based only on the available "
                "visual evidence. A clearer image or more specific "
                "question may help."
            )

        # Save history
        st.session_state.history.append(("User", question))
        st.session_state.history.append(("Assistant", response))

        st.subheader("Assistant Response")
        st.write(response)


st.divider()

st.subheader("Conversation History")

for role, msg in st.session_state.history:
    st.write(f"**{role}:** {msg}")