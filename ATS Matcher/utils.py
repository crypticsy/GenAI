import pdfplumber


# --- PDF Resume Extract ---
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# --- Tool: Keyword Extractor ---
def extract_keywords(resume, jd):
    return f"Resume Keywords:\n{', '.join(set(resume.lower().split()) & set(jd.lower().split()))}"


# --- Tool: Simple Match Score (token overlap) ---
def match_score(resume, jd):
    resume_words = set(resume.lower().split())
    jd_words = set(jd.lower().split())
    overlap = resume_words & jd_words
    return f"Keyword Match Score: {len(overlap)} / {len(jd_words)} ({(len(overlap)/len(jd_words))*100:.2f}%)"
