import streamlit as st
from services.extractor import extract_text
from services.llm_client import call_ollama
from utils.prompts import SYSTEM_PROMPT

st.title("📝 Resume Analyzer (Local AI • Free • Powered by Ollama)")

uploaded = st.file_uploader("Upload your Resume (PDF / DOCX / TXT)", type=["pdf", "docx", "txt"])

if uploaded:
    st.success("File uploaded successfully!")
    resume_text = extract_text(uploaded)

    st.subheader("Extracted Resume Text")
    st.text_area("Resume Content:", resume_text, height=200)

    question = st.text_input("Ask anything about the resume:")

    if st.button("Analyze"):
        with st.spinner("Thinking..."):
            prompt = f"{SYSTEM_PROMPT}\n\nResume:\n{resume_text}\n\nQuestion: {question}"
            answer = call_ollama(prompt)
            st.subheader("Answer:")
            st.write(answer)
