# app.py

import streamlit as st
from resume_parser import extract_text_from_resume
from skills_extraction import extract_skills
from scoring import calculate_score

st.title("AI-Powered Resume Screening System")
st.write("Upload a resume and get skill-based evaluation")

# Job skills input
job_skills_input = st.text_area("Enter required job skills (comma separated)", "python, sql, machine learning")
job_skills = [skill.strip() for skill in job_skills_input.split(",")]

# File uploader
uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    st.success(f"Resume uploaded: {uploaded_file.name}")
    
    # Extract text
    text = extract_text_from_resume(uploaded_file)
    
    # Extract skills
    resume_skills = extract_skills(text)
    
    # Score calculation
    score, matched_skills = calculate_score(resume_skills, job_skills)
    
    # Display results
    st.subheader("Resume Skills Extracted")
    st.write(resume_skills)
    
    st.subheader("Matched Skills with Job Requirements")
    st.write(matched_skills)
    
    st.subheader("Resume Match Score")
    st.write(f"{score}%")
