import streamlit as st
import pandas as pd

from modules.clinical_ner import extract_clinical_entities
from modules.disease_surveillance import analyze_disease_signal
from modules.cdss import generate_cdss_alerts
from modules.feedback_analysis import analyze_patient_feedback
from modules.deidentification import deidentify_ehr_text


st.set_page_config(
    page_title="MediNLP Suite",
    page_icon="🩺",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .hero {
        background: linear-gradient(135deg, #0f766e, #2563eb);
        padding: 35px;
        border-radius: 22px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    }

    .hero h1 {
        font-size: 46px;
        margin-bottom: 5px;
    }

    .hero p {
        font-size: 18px;
        opacity: 0.95;
    }

    .feature-card {
        background-color: white;
        padding: 20px;
        border-radius: 18px;
        box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
        border-left: 6px solid #0f766e;
        margin-bottom: 18px;
    }

    .footer {
        text-align: center;
        padding: 25px;
        margin-top: 40px;
        color: #475569;
        background-color: white;
        border-radius: 18px;
        box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
    }

    .footer a {
        color: #2563eb;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="hero">
        <h1>🩺 MediNLP Suite</h1>
        <p>AI-Powered Healthcare NLP Platform for Clinical Text Intelligence</p>
        <p><b>Clinical NER • Disease Surveillance • CDSS • Sentiment Analysis • EHR De-identification</b></p>
    </div>
    """,
    unsafe_allow_html=True
)


with st.sidebar:
    st.title("🧠 MediNLP")
    st.write("A professional Healthcare NLP platform built using Python, Streamlit, spaCy, and NLP techniques.")
    st.markdown("---")
    st.subheader("Project Modules")
    st.write("✅ Clinical NER")
    st.write("✅ Disease Surveillance")
    st.write("✅ Clinical Decision Support")
    st.write("✅ Patient Feedback Analysis")
    st.write("✅ EHR De-identification")
    st.markdown("---")
    st.info("This project is designed for healthcare AI demonstration SRMIST.")


tabs = st.tabs([
    "🧬 Clinical NER",
    "🌍 Disease Surveillance",
    "🚨 CDSS",
    "💬 Patient Feedback",
    "🔐 EHR De-identification"
])


with tabs[0]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.header("🧬 Clinical Named Entity Recognition")
    st.write("Extract diseases, symptoms, medications, procedures, and clinical entities from unstructured medical text.")

    text = st.text_area(
        "Enter clinical note",
        "Patient has fever, chest pain and diabetes. Doctor prescribed aspirin 325mg and insulin.",
        height=160
    )

    if st.button("Extract Clinical Entities", use_container_width=True):
        entities = extract_clinical_entities(text)

        if entities:
            st.success("Entities extracted successfully.")
            st.dataframe(pd.DataFrame(entities), use_container_width=True)
        else:
            st.info("No entities detected.")
    st.markdown('</div>', unsafe_allow_html=True)


with tabs[1]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.header("🌍 Disease Surveillance and Early Signal Detection")
    st.write("Analyze public health reports, hospital notes, or social media text to detect possible disease signals.")

    surveillance_text = st.text_area(
        "Enter surveillance text",
        "Many patients in Chennai are reporting fever, cough, breathing difficulty and sore throat.",
        height=160
    )

    if st.button("Analyze Disease Signal", use_container_width=True):
        result = analyze_disease_signal(surveillance_text)

        col1, col2 = st.columns(2)
        col1.metric("Risk Score", result["risk_score"])
        col2.metric("Risk Level", result["risk_level"])

        st.write("Detected Terms:", result["detected_terms"])
        st.write("Categories:", result["categories"])

        if result["risk_level"] == "High":
            st.error(result["recommendation"])
        elif result["risk_level"] == "Moderate":
            st.warning(result["recommendation"])
        else:
            st.info(result["recommendation"])

    st.markdown('</div>', unsafe_allow_html=True)


with tabs[2]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.header("🚨 Clinical Decision Support System")
    st.write("Generate clinical alerts from patient condition text using NLP-supported decision logic.")

    cdss_text = st.text_area(
        "Enter patient condition",
        "Patient has chest pain, sweating and shortness of breath.",
        height=160
    )

    if st.button("Generate CDSS Alerts", use_container_width=True):
        result = generate_cdss_alerts(cdss_text)

        for alert in result["alerts"]:
            if alert["severity"] == "High":
                st.error(f"🚨 {alert['condition']}")
            elif alert["severity"] == "Moderate":
                st.warning(f"⚠️ {alert['condition']}")
            else:
                st.info(f"ℹ️ {alert['condition']}")

            st.write("**Severity:**", alert["severity"])
            st.write("**Recommendation:**", alert["recommendation"])
            st.markdown("---")

        st.caption(result["disclaimer"])

    st.markdown('</div>', unsafe_allow_html=True)


with tabs[3]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.header("💬 Patient Feedback and Sentiment Analysis")
    st.write("Analyze patient feedback sentiment and detect service quality aspects.")

    feedback = st.text_area(
        "Enter patient feedback",
        "The doctor was kind and explained well, but the waiting time was too long.",
        height=160
    )

    if st.button("Analyze Feedback", use_container_width=True):
        result = analyze_patient_feedback(feedback)

        col1, col2, col3 = st.columns(3)
        col1.metric("Sentiment", result["sentiment"])
        col2.metric("Polarity", result["polarity"])
        col3.metric("Subjectivity", result["subjectivity"])

        st.write("Detected Aspects:", result["detected_aspects"])

    st.markdown('</div>', unsafe_allow_html=True)


with tabs[4]:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.header("🔐 EHR De-identification")
    st.write("Remove Protected Health Information such as names, phone numbers, emails, dates, and patient IDs.")

    ehr_text = st.text_area(
        "Enter EHR text",
        "Patient John Kumar, age 45, phone 9876543210, email john@gmail.com, visited on 12/04/2026. MRN: A12345.",
        height=160
    )

    if st.button("De-identify EHR Text", use_container_width=True):
        result = deidentify_ehr_text(ehr_text)

        st.subheader("De-identified Text")
        st.success(result["deidentified_text"])

        st.subheader("PHI Detection Summary")
        st.dataframe(
            pd.DataFrame(result["phi_counts"].items(), columns=["PHI Type", "Count"]),
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)


st.markdown(
    """
    <div class="footer">
        <h3>👨‍💻 Developed by Gershom Richard Bruno</h3>
        <p>Biomedical Engineering | AI in Healthcare | NLP Project</p>
        <p>🔗 <a href="https://linktr.ee/gershomrichardbruno" target="_blank">Visit my Linktree</a></p>
    </div>
    """,
    unsafe_allow_html=True
)