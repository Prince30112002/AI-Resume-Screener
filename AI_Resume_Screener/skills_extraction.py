import re

# Predefined skill set (you can expand this anytime)
SKILLS_DB = [
    "python", "java", "c++", "sql", "mysql", "postgresql",
    "machine learning", "deep learning", "data science",
    "data analysis", "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch", "nlp", "computer vision",
    "statistics", "matplotlib", "seaborn",
    "power bi", "tableau", "excel",
    "git", "github", "docker", "aws", "azure",
    "flask", "streamlit", "fastapi"
]

def extract_skills(resume_text):
    """
    Extract skills from resume text
    :param resume_text: cleaned resume text
    :return: list of matched skills
    """
    found_skills = set()

    for skill in SKILLS_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume_text):
            found_skills.add(skill)

    return sorted(found_skills)
