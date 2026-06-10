# Career Mentor Agent starting point

# Function to extract text from a resume PDF
import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text
  if __name__ == "__main__":
    resume_text = extract_text_from_pdf("resume.pdf")
    print(resume_text)

