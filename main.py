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


