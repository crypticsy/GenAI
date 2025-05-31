from langchain_ollama import OllamaLLM  # Make sure this import matches your package

# Query Ollama for comparison and suggestions
def query_llm(resume_text, job_description):
    prompt = f"""
You are an expert in resume screening and ATS optimization.

Evaluate how well the following resume matches the given job description. 
Provide:

1. A match rating (0 to 100)
2. A short explanation of the score
3. 3-5 suggestions to improve the resume for better ATS performance

### Resume:
{resume_text}

### Job Description:
{job_description}
"""

    llm = OllamaLLM(model='llama3')  # Initialize the LLM object
    response = llm.invoke(prompt)  # Use `.invoke()` to get a response

    return response  # Should be plain text or markdown-compatible string