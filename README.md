
# 🤖 AI-Powered Resume Screening System

An AI-based Resume Screening System that analyzes resumes and evaluates them against required job skills.  
This project uses **Python** and **Streamlit** to extract skills from resumes (PDF/DOCX) and calculate a matching score.

---

## 📌 Overview

Recruiters receive hundreds of resumes for a single role. Manually screening them is time-consuming and inefficient.  
This project automates resume screening by:

- Extracting skills from resumes
- Matching them with job requirements
- Calculating a resume match score
- Displaying results through an interactive web interface

---

## 🎯 Business Problem

Manual resume screening:
- Is slow and error-prone
- Misses relevant candidates
- Lacks standard evaluation criteria

### ✅ Solution

This AI-powered system:
- Automatically parses resumes
- Identifies relevant skills
- Scores resumes objectively
- Helps shortlist candidates faster

---

## 📂 Dataset / Input

- Resume files in **PDF** or **DOCX** format  
- Job skills entered manually (comma-separated)

**Example:**
```text
python, sql, machine learning
````

---

## 🛠️ Tools & Technologies

* **Python**
* **Streamlit** (Web App)
* **PDF & DOCX Parsing**
* **Text Processing (NLP basics)**
* **Git & GitHub**

---

## 📁 Project Structure

```
AI_Resume_Screener/
│
├── app.py
├── resume_parser.py
├── skills_extraction.py
├── scoring.py
├── requirements.txt
├── README.md
│
├── resumes/
│   ├── resume1.pdf
│   └── resume2.docx
│
└── utils/
    └── custom_functions.py
```

---

## 🔍 Features

* Upload resume (PDF/DOCX)
* Enter required job skills
* Extract skills automatically from resume
* Match resume skills with job requirements
* Generate resume match score
* Simple and clean UI

---

## 📸 Application Output

<p align="center">
  <img src="assets/output.png" alt="AI Resume Screener Output" width="800"/>
</p>

---

## ⚙️ How It Works

1. User uploads a resume
2. Resume text is extracted
3. Skills are identified from resume text
4. Job-required skills are compared
5. Match score is calculated
6. Results are displayed on the web app

---

## ▶️ How to Run This Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Prince30112002/AI-Resume-Screener.git
cd AI-Resume-Screener
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run app.py
```

### 4️⃣ Open in browser

```
http://localhost:8501
```

---

## 📊 Resume Match Scoring Logic

```
Match Score (%) = (Matched Skills / Required Skills) * 100
```

**Example:**

* Required Skills: Python, SQL, ML
* Matched Skills: Python, ML
* Score: **66.67%**

---

## 🚀 Future Improvements

* Improve NLP using spaCy / Transformers
* Add experience & education scoring
* Support multiple resumes at once
* Integrate ATS-style ranking
* Deploy on cloud (AWS / Streamlit Cloud)

---

## 👨‍💻 Author

**Prince Rajak**
Computer Science Student | Machine Learning Enthusiast

📧 Email: **[rajakprince30112002@gmail.com](mailto:rajakprince30112002@gmail.com)**
🔗 GitHub: [https://github.com/Prince30112002](https://github.com/Prince30112002)

---

