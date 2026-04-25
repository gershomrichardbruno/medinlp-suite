# 🩺 MediNLP Suite – Healthcare NLP Platform

An end-to-end Healthcare Natural Language Processing (NLP) web application that converts unstructured clinical text into structured medical insights.

##  Features

### 1. Clinical Named Entity Recognition (NER)
- Extracts diseases, symptoms, medications, and procedures
- Combines spaCy NLP + custom medical dictionary

### 2. Disease Surveillance
- Detects early disease signals from text
- Classifies risk levels (Low / Moderate / High)

### 3. Clinical Decision Support System (CDSS)
- Generates alerts for critical conditions
- Provides rule-based medical recommendations

### 4. Patient Feedback Analysis
- Sentiment analysis (Positive / Neutral / Negative)
- Aspect detection (waiting time, billing, staff behavior)

### 5. EHR De-identification
- Removes sensitive patient information (PHI)
- Ensures privacy compliance

---

##  Tech Stack

- Python 3.10
- Streamlit
- spaCy
- TextBlob
- Pandas

---

##  Project Structure


medinlp-suite/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│ ├── clinical_ner.py
│ ├── disease_surveillance.py
│ ├── cdss.py
│ ├── feedback_analysis.py
│ └── deidentification.py


---

##  How to Run

```bash
git clone <your-repo-link>
cd medinlp-suite
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

Use Case

This system demonstrates how NLP can:

Convert clinical text into structured data
Support medical decision-making
Detect disease trends
Improve healthcare quality analysis
⚠️ Disclaimer

This project is for educational and demonstration purposes only and is not intended for real medical diagnosis.

👨‍💻 Author

Developed by [Gershom Richard Bruno]
🔗 Linktree: https://linktr.ee/gershomrichardbruno