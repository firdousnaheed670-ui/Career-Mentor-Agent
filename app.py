import streamlit as st
from PyPDF2 import PdfReader
import re

# Function to extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    reader = PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract keywords from JD
def extract_keywords_from_jd(jd_text):
    potential_keywords = re.findall(r'\b[A-Z][a-zA-Z0-9\+\#]*\b', jd_text)
    stopwords = {"The", "And", "With", "For", "In", "On", "Of"}
    keywords = [word for word in potential_keywords if word not in stopwords]
    return list(set(keywords))

# Streamlit UI
st.title("🧑‍💼 Career Mentor Agent")
st.write("Upload your Resume and Job Description PDFs to compare skills.")

resume_file = st.file_uploader("Upload Resume PDF", type="pdf")
jd_file = st.file_uploader("Upload Job Description PDF", type="pdf")

if resume_file and jd_file:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)

    jd_keywords = extract_keywords_from_jd(jd_text)
    found = [kw for kw in jd_keywords if kw.lower() in resume_text.lower()]
    missing = [kw for kw in jd_keywords if kw.lower() not in resume_text.lower()]

    st.subheader("✅ Skills Found in Resume")
    st.write(found)

    st.subheader("⚠️ Skills Missing from Resume")
    st.write(missing)

    st.subheader("💡 Career Advice")
    for skill in missing:
        if skill.lower() == "aws":
            st.write("- Add cloud experience (AWS/Azure/GCP).")
        elif skill.lower() == "tensorflow":
            st.write("- Highlight ML projects using TensorFlow or PyTorch.")
        elif skill.lower() == "tableau":
            st.write("- Add Tableau dashboards to complement Power BI.")
        else:
            st.write(f"- Consider gaining experience with {skill}.")
