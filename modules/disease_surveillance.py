from typing import Dict, List


SURVEILLANCE_SYMPTOMS = {
    "respiratory": ["fever", "cough", "breathing difficulty", "shortness of breath", "sore throat"],
    "gastrointestinal": ["diarrhea", "vomiting", "stomach pain", "nausea"],
    "neurological": ["headache", "dizziness", "confusion", "seizure"],
    "skin": ["rash", "itching", "red spots"],
}


def analyze_disease_signal(text: str) -> Dict:
    text_lower = text.lower()
    detected_terms: List[str] = []
    detected_categories: List[str] = []

    for category, symptoms in SURVEILLANCE_SYMPTOMS.items():
        for symptom in symptoms:
            if symptom in text_lower:
                detected_terms.append(symptom)
                if category not in detected_categories:
                    detected_categories.append(category)

    score = len(detected_terms)

    if score >= 4:
        risk_level = "High"
        recommendation = "Possible disease cluster detected. Public health monitoring is recommended."
    elif score >= 2:
        risk_level = "Moderate"
        recommendation = "Multiple symptoms detected. Continue observation and collect more reports."
    elif score == 1:
        risk_level = "Low"
        recommendation = "Single symptom detected. No strong outbreak signal."
    else:
        risk_level = "Minimal"
        recommendation = "No major disease surveillance signal detected."

    return {
        "detected_terms": detected_terms,
        "categories": detected_categories,
        "risk_score": score,
        "risk_level": risk_level,
        "recommendation": recommendation,
    }