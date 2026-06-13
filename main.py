# Career Mentor Agent - Step 2: Resume Text Extraction

import PyPDF2
import re

# Function to extract text from a resume PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text

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

# Function to extract skills and keywords from resume text
def extract_skills(resume_text):
    found_skills = [skill for skill in ALL_SKILLS if skill.lower() in resume_text.lower()]
    missing_skills = [skill for skill in ALL_SKILLS if skill.lower() not in resume_text.lower()]
    return found_skills, missing_skills
# Comparing Resume with JD
def extract_keywords_from_jd(jd_text):
    jd_keywords = [skill for skill in ALL_SKILLS if skill.lower() in jd_text.lower()]
    return jd_keywords

def compare_resume_with_jd(resume_path, jd_path):
    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_pdf(jd_path)

    jd_keywords = extract_keywords_from_jd(jd_text)

    found = [kw for kw in jd_keywords if kw.lower() in resume_text.lower()]
    missing = [kw for kw in jd_keywords if kw.lower() not in resume_text.lower()]
    print("✅ Skills matching JD:", found)
    print("⚠️ Skills missing from resume:", missing)
    return found, missing
# To Generate Career Advice
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

#Run the Agent
    if __name__ == "__main__":
    resume_path = "Sample Resumes/Data_Analyst_resume_updated.pdf"
    jd_path = "JobDescriptions/Data_Analyst_JD.pdf"

    # Extract resume text
    resume_text = extract_text_from_pdf(resume_path)

    # Find skills
    found, missing = extract_skills(resume_text)
    print("✅ Skills found in resume:", found)
    print("⚠️ Skills missing from resume:", missing)

    # Compare with JD
    jd_found, jd_missing = compare_resume_with_jd(resume_path, jd_path)

    # Generate career advice
    advice = generate_career_advice(jd_missing)
    print("\n💡 Career Advice:")
    for tip in advice:
        print("-", tip)

import spacy
nlp = spacy.load("en_core_web_sm")

def extract_keywords_from_jd(jd_text):
    doc = nlp(jd_text)
    keywords = [token.text for token in doc if token.pos_ in ["PROPN", "NOUN"]]
    # Filter obvious junk
    stopwords = {"Job", "Description", "Responsibilities", "Required", "What", "You"}
    return [kw for kw in keywords if kw not in stopwords]

    

   

