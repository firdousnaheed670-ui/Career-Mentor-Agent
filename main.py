# Career Mentor Agent starting point

# Function to extract text from a resume PDF
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

# Test the function with your single sample resume
if __name__ == "__main__":
    resume_text = extract_text_from_pdf("samples/resume.pdf")
    print("Extracted Resume Text:\n")
    print(resume_text)


