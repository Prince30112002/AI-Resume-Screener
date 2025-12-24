# resume_parser.py

from PyPDF2 import PdfReader
import docx2txt

def extract_text_from_resume(file):
    """
    Extract text from uploaded resume (PDF or DOCX)
    
    :param file: file path or Streamlit uploaded file
    :return: text content of resume
    """
    file_name = getattr(file, "name", file)  # Streamlit file object or path
    file_type = file_name.split(".")[-1].lower()
    
    text = ""
    
    if file_type == "pdf":
        # PDF: open in binary mode
        f = file if isinstance(file, str) else file
        reader = PdfReader(f if isinstance(f, str) else f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
            
    elif file_type == "docx":
        # DOCX
        path = file if isinstance(file, str) else file.name
        text = docx2txt.process(path)
    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are allowed.")
    
    return text
