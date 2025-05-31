# Import necessary libraries
import streamlit as st  # For building the web app UI
from llm import query_llm  # Custom function to query the LLM
from utils import extract_text_from_pdf  # Custom function to extract text from a PDF

# Configure the Streamlit page
st.set_page_config(
    page_title="ATS Matcher",  # Title of the browser tab
    page_icon="🧠",  # Favicon icon
    layout="wide",  # Use the full width of the screen
    initial_sidebar_state="collapsed",  # Collapse the sidebar by default
)

# Apply custom CSS to remove excess whitespace and add padding
st.markdown(
    """
        <style>
               .block-container {
                    padding-top: 3rem;
                    padding-bottom: 3rem;
                    padding-left: 6vw;
                    padding-right: 6vw;
                }
        </style>
        """,
    unsafe_allow_html=True,
)

# Main heading and instructions
st.subheader("🧠 LLM-Powered ATS Matcher", divider="red")
st.markdown(
    "Upload your resume and paste a job description. The LLM will rate your match and suggest improvements."
)
st.markdown(unsafe_allow_html=True, body="<br/>")  # Add spacing below the markdown

# File uploader widget for uploading the resume (PDF only)
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])
st.markdown(unsafe_allow_html=True, body="<br/>")  # Add spacing below the file uploader

# Text area for pasting the job description
job_description = st.text_area("📝 Paste Job Description", height=300)

# If both a resume and job description are provided, process them
if uploaded_file and job_description:
    with st.spinner(
        "🤖 Analyzing with LLM..."
    ):  # Show a loading spinner while processing
        resume_text = extract_text_from_pdf(
            uploaded_file
        )  # Extract text from the uploaded PDF
        analysis = query_llm(
            resume_text, job_description
        )  # Query the LLM with the resume and job description

    # Display the LLM's feedback
    st.subheader("Feedback:")
    st.markdown(analysis)
