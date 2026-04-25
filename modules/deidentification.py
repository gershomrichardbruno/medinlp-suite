import re
from typing import Dict


def deidentify_ehr_text(text: str) -> Dict:
    deidentified = text

    patterns = {
        "EMAIL": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
        "PHONE": r"\b\d{10}\b",
        "DATE": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        "ID": r"\b(?:MRN|ID|Patient ID|Reg No)\s*[:\-]?\s*[A-Za-z0-9]+\b",
        "AGE": r"\b(?:age|aged)\s+\d{1,3}\b",
        "NAME": r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b",
    }

    counts = {}

    for label, pattern in patterns.items():
        matches = re.findall(pattern, deidentified)
        counts[label] = len(matches)
        deidentified = re.sub(pattern, f"[{label}]", deidentified)

    return {
        "original_text": text,
        "deidentified_text": deidentified,
        "phi_counts": counts,
    }