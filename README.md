# Career Mentor Agent 🎯

A Python-based tool that helps job seekers align their resumes with job descriptions (JDs).  
It extracts text from resumes and JDs, compares skills, and provides actionable career advice to close gaps.
---
## 📌 Problem Statement
Job seekers often struggle to tailor their resumes to match job descriptions (JDs).  
Recruiters look for specific skills, but resumes may miss critical keywords or highlight irrelevant ones.  
This project helps bridge that gap by automatically comparing resumes with JDs and providing actionable career advice.

---
## 🚀 Live Demo
Try the app here: [Open Live Demo](https://career-mentor-agent-ngbfajqlm9dwigsgsp3ajm.streamlit.app/) 
---
## 📊 Datasets / Inputs
- **Resume PDF**: Candidate’s resume file.  
- **Job Description PDF**: Target JD file.
The agent extracts text from both, compares skills, and highlights matches and gaps.
---
## 🔍 Key Insights
- ✅ Identifies skills present in the resume that match the JD.  
- ⚠️ Highlights missing skills that should be added.  
- 💡 Provides career advice on how to close skill gaps (e.g., projects, certifications, tools).  
- Works dynamically with **any resume and JD PDF**.

---
## 🛠️ Tech Stack
- **Python 3**  
- **PyPDF2**   
- **Regex** 
-  Streamlit

---


## 📂 Project Structure
```bash
Career-Mentor-Agent/
│
├── main.py                     
├── requirements.txt            
├── README.md                    
│
├── Sample Resumes/             
│   └── Data_Analyst_resume_updated.pdf
│
└── JobDescriptions/            
     └── Data Analyst JD.pdf
```

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/Career-Mentor-Agent.git
cd Career-Mentor-Agent
pip install -r requirements.txt
```
---

▶️ Usage
Run the script locally:
python main.py
---
Example Output
✅ Skills found in resume: ['Python', 'SQL', 'Power BI', 'Excel', 'Machine Learning', 'Deep Learning']
⚠️ Skills missing from resume: ['AWS', 'TensorFlow', 'Tableau']

💡 Career Advice:
- Consider adding cloud experience (AWS/Azure/GCP) to align with industry expectations.
- Highlight ML projects using TensorFlow or PyTorch to show deep learning expertise.
- Add Tableau dashboards to complement Power BI.

---
📊 Results
Clear identification of resume strengths.

Pinpointed missing skills aligned with JD requirements.

Actionable career advice for improvement.

---
🔮 Future Work
Add a scoring system (e.g., Resume matches 70% of JD skills).

Compare against multiple JDs in one run.

Visualize results with charts (matched vs missing skills).

Integrate with LinkedIn job postings for real-time analysis.

---
🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---
📜 License
This project is licensed under the MIT License.

---



