from typing import Dict, List


def generate_cdss_alerts(text: str) -> Dict:
    text_lower = text.lower()
    alerts: List[Dict[str, str]] = []

    if "chest pain" in text_lower and (
        "shortness of breath" in text_lower or "sweating" in text_lower
    ):
        alerts.append({
            "severity": "High",
            "condition": "Possible cardiac emergency",
            "recommendation": "Recommend immediate ECG, vital monitoring, and physician evaluation."
        })

    if "fever" in text_lower and ("cough" in text_lower or "sore throat" in text_lower):
        alerts.append({
            "severity": "Moderate",
            "condition": "Possible respiratory infection",
            "recommendation": "Recommend temperature monitoring, oxygen saturation check, and clinical review."
        })

    if "diabetes" in text_lower and ("insulin" in text_lower or "metformin" in text_lower):
        alerts.append({
            "severity": "Moderate",
            "condition": "Diabetes medication monitoring",
            "recommendation": "Monitor blood glucose levels and check medication adherence."
        })

    if "allergy" in text_lower and ("amoxicillin" in text_lower or "penicillin" in text_lower):
        alerts.append({
            "severity": "High",
            "condition": "Possible drug allergy risk",
            "recommendation": "Verify allergy history before prescribing antibiotic."
        })

    if not alerts:
        alerts.append({
            "severity": "Low",
            "condition": "No critical alert detected",
            "recommendation": "Continue routine clinical observation."
        })

    return {
        "alerts": alerts,
        "disclaimer": "This CDSS module is for educational and decision-support demonstration only. It is not a replacement for professional medical diagnosis."
    }