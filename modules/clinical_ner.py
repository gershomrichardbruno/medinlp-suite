import spacy
from typing import List, Dict

try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = spacy.blank("en")


MEDICAL_TERMS = {
    "DISEASE": [
        "diabetes", "hypertension", "asthma", "pneumonia",
        "tuberculosis", "covid", "cancer", "anemia", "migraine"
    ],
    "SYMPTOM": [
        "fever", "cough", "chest pain", "headache",
        "breathing difficulty", "fatigue", "vomiting",
        "diarrhea", "dizziness"
    ],
    "MEDICATION": [
        "aspirin", "insulin", "metformin", "paracetamol",
        "amoxicillin", "atorvastatin", "salbutamol"
    ],
    "PROCEDURE": [
        "x-ray", "ct scan", "mri", "ecg", "blood test", "surgery"
    ]
}


def extract_clinical_entities(text: str) -> List[Dict[str, str]]:
    doc = nlp(text)
    results = []

    for ent in doc.ents:
        results.append({
            "text": ent.text,
            "label": ent.label_,
            "source": "spaCy NER"
        })

    lower_text = text.lower()

    for label, terms in MEDICAL_TERMS.items():
        for term in terms:
            if term in lower_text:
                results.append({
                    "text": term,
                    "label": label,
                    "source": "Medical Dictionary"
                })

    return results