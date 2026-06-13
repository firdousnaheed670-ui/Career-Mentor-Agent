import streamlit as st
from PyPDF2 import PdfReader

# Curated skills for Data Analyst & Data Scientist roles
DATA_ANALYST_SKILLS = [
    "Python", "SQL", "Excel", "Power BI", "Tableau", "R", "Statistics",
    "Data Cleaning", "EDA", "Data Visualization", "Business Intelligence",
    "Reporting", "Dashboards"
]

DATA_SCIENTIST_SKILLS = [
    "Python", "R", "SQL", "Machine Learning", "Deep Learning", "TensorFlow",
    "PyTorch", "Scikit-learn", "Statistics", "Data Mining", "Feature Engineering",
    "Model Deployment", "Big Data", "Hadoop", "Spark", "AWS", "Azure", "GCP"
]

ALL_SKILLS = list(set(DATA_ANALYST_SKILLS + DATA_SCIENTIST_SKILLS))

# Function to extract text from PDF
def extract_text_from_pdf(file):
    text = ""
    reader = PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract skills from JD text
def extract_keywords_from_jd(jd_text):
    jd_keywords = [skill for skill in ALL_SKILLS if skill.lower() in jd_text.lower()]
    return jd_keywords

# Function to generate career advice
def generate_career_advice(missing_skills):
    advice = []
    for skill in missing_skills:
        if skill == "AWS":
            advice.append("Add cloud experience (AWS/Azure/GCP) to strengthen data pipeline skills.")
        elif skill == "TensorFlow":
            advice.append("Highlight ML projects using TensorFlow or PyTorch to show deep learning expertise.")
        elif skill == "Tableau":
            advice.append("Add Tableau dashboards to complement Power BI for visualization variety.")
        elif skill == "Statistics":
            advice.append("Showcase statistical analysis projects to demonstrate strong analytical foundation.")
        else:
            advice.append(f"Consider gaining experience with {skill} and including it in your resume.")
    return advice

# Streamlit UI
st.title("🧑‍💼 Career Mentor Agent")
# Streamlit UI
role = st.selectbox("Select Role", ["Data Analyst", "Data Scientist"])

if role == "Data Analyst":
    st.title("📊 Career Mentor Agent – Data Analyst Role")
    skills_list = DATA_ANALYST_SKILLS
else:
    st.title("🧪 Career Mentor Agent – Data Scientist Role")
    skills_list = DATA_SCIENTIST_SKILLS

st.write("Upload your Resume and Job Description PDFs to compare skills.")

resume_file = st.file_uploader("Upload Resume PDF", type="pdf")
jd_file = st.file_uploader("Upload Job Description PDF", type="pdf")

if resume_file and jd_file:
    resume_text = extract_text_from_pdf(resume_file)
    jd_text = extract_text_from_pdf(jd_file)

    jd_keywords = [skill for skill in skills_list if skill.lower() in jd_text.lower()]
    found = [kw for kw in jd_keywords if kw.lower() in resume_text.lower()]
    missing = [kw for kw in jd_keywords if kw.lower() not in resume_text.lower()]

    st.subheader("✅ Skills Found in Resume")
    st.write(found)

    st.subheader("⚠️ Skills Missing from Resume")
    st.write(missing)

    st.subheader("💡 Career Advice")
    advice = generate_career_advice(missing)
    for tip in advice:
        st.write("-", tip)



