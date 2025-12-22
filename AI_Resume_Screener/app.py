import streamlit as st

st.set_page_config(
    page_title="AI Resume Screener",
    page_icon="📄",
    layout="centered"
)

st.title("AI-Powered Resume Screening System")
st.write("Upload a resume and get skill-based evaluation")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
