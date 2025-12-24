# skills_extraction.py

import re

# Simple skill list (tum apne hisaab se expand kar sakte ho)
SKILL_SET = [
    "python", "sql", "excel", "machine learning", "data analysis",
    "power bi", "tableau", "deep learning", "nlp", "pandas",
    "numpy", "scikit-learn", "tensorflow", "keras"
]

def extract_skills(text):
    """
    Extract skills from resume text
    :param text: extracted resume text
    :return: list of found skills
    """
    text_lower = text.lower()
    skills_found = []

    for skill in SKILL_SET:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text_lower):
            skills_found.append(skill)
    
    return skills_found
