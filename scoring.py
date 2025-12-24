# scoring.py

def calculate_score(resume_skills, job_skills):
    """
    Calculate resume match score
    """
    if not job_skills:
        return 0, []

    matched_skills = set(resume_skills).intersection(set(job_skills))
    score = (len(matched_skills) / len(job_skills)) * 100
    return round(score, 2), list(matched_skills)
