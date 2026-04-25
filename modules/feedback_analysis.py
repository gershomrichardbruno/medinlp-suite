from typing import Dict, List
from textblob import TextBlob


ASPECT_KEYWORDS = {
    "Waiting Time": ["waiting", "delay", "late", "queue", "long time"],
    "Doctor Communication": ["doctor", "explained", "kind", "rude", "communication"],
    "Billing": ["bill", "payment", "cost", "expensive", "charges"],
    "Cleanliness": ["clean", "dirty", "hygiene", "washroom"],
    "Staff Behaviour": ["staff", "nurse", "reception", "attitude", "helpful"],
}


def analyze_patient_feedback(text: str) -> Dict:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    text_lower = text.lower()
    detected_aspects: List[str] = []

    for aspect, keywords in ASPECT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                detected_aspects.append(aspect)
                break

    return {
        "sentiment": sentiment,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
        "detected_aspects": detected_aspects,
    }