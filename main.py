# Career Mentor Agent - Step 2: Resume Text Extraction

import PyPDF2

# Function to extract text from a resume PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Test the function with your uploaded resume
if __name__ == "__main__":
    resume_text = extract_text_from_pdf("Sample Resumes/Data_Analyst_resume_updated.pdf")
    print("Extracted Resume Text:\n")
    print(resume_text)
# Function to extract skills and keywords from resume text
def extract_skills(resume_text):
    keywords = ["Python", "SQL", "Power BI", "Excel", "Machine Learning", "Deep Learning", "AWS", "TensorFlow"]
    found_skills = [skill for skill in keywords if skill.lower() in resume_text.lower()]
    missing_skills = [skill for skill in keywords if skill.lower() not in resume_text.lower()]
    return found_skills, missing_skills

if __name__ == "__main__":
    resume_text = extract_text_from_pdf("Sample Resumes/Data_Analyst_resume_updated.pdf")
    found, missing = extract_skills(resume_text)
    print("✅ Skills found in resume:", found)
    print("⚠️ Skills missing from resume:", missing)
def compare_resume_with_jd(resume_path, jd_path):
    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_pdf(jd_path)

    # Define keywords you want to check
    jd_keywords = ["Python", "R", "SQL", "Power BI", "AWS", "TensorFlow", "Tableau", "Statistics", "Machine Learning"]

    found = [kw for kw in jd_keywords if kw.lower() in resume_text.lower()]
    missing = [kw for kw in jd_keywords if kw.lower() not in resume_text.lower()]

    print("✅ Skills matching JD:", found)
    print("⚠️ Skills missing from resume:", missing)

if __name__ == "__main__":
    compare_resume_with_jd(
        "Sample Resumes/Data_Analyst_resume_updated.pdf",
        "JobDescriptions/Data Analyst JD.pdf"
    )

def generate_career_advice(missing_skills):
    advice = []
    for skill in missing_skills:
        if skill == "AWS":
            advice.append("Consider adding cloud experience (AWS/Azure/GCP) to align with industry expectations.")
        elif skill == "TensorFlow":
            advice.append("Highlight ML projects using TensorFlow or PyTorch to show deep learning expertise.")
        elif skill == "Tableau":
            advice.append("Add Tableau or advanced visualization tools to complement Power BI.")
        else:
            advice.append(f"Consider gaining experience with {skill} and including it in your resume.")
    return advice

if __name__ == "__main__":
    resume_path = "Sample Resumes/Data_Analyst_resume_updated.pdf"
    jd_path = "JobDescriptions/Data_Analyst_JD.pdf"
    resume_text = extract_text_from_pdf(resume_path)
    found, missing = extract_skills(resume_text)
    print("✅ Skills found in resume:", found)
    print("⚠️ Skills missing from resume:", missing)
    advice = generate_career_advice(missing)
    print("\n💡 Career Advice:")
    for tip in advice:
        print("-", tip)

import re

def extract_keywords_from_jd(jd_text):
    # Simple approach: look for capitalized words or tech terms
    potential_keywords = re.findall(r'\b[A-Z][a-zA-Z0-9\+\#]*\b', jd_text)
    # Filter out common words
    stopwords = {"The", "And", "With", "For", "In", "On", "Of"}
    keywords = [word for word in potential_keywords if word not in stopwords]
    return list(set(keywords))

def compare_resume_with_jd(resume_path, jd_path):
    resume_text = extract_text_from_pdf(resume_path)
    jd_text = extract_text_from_pdf(jd_path)

    jd_keywords = extract_keywords_from_jd(jd_text)

    found = [kw for kw in jd_keywords if kw.lower() in resume_text.lower()]
    missing = [kw for kw in jd_keywords if kw.lower() not in resume_text.lower()]

    print("✅ Skills matching JD:", found)
    print("⚠️ Skills missing from resume:", missing)

