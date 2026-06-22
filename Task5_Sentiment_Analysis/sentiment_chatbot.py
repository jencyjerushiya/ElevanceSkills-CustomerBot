from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0.2:
        sentiment = "Positive 😊"
        response = (
            "Thank you for your positive feedback! "
            "We're happy to know you're having a good experience."
        )

    elif polarity < -0.2:
        sentiment = "Negative 😔"
        response = (
            "We're sorry to hear about your experience. "
            "Your feedback is important, and we appreciate you sharing it."
        )

    else:
        sentiment = "Neutral 😐"
        response = (
            "Thank you for your message. "
            "Please let us know if you need any further assistance."
        )

    return sentiment, polarity, response