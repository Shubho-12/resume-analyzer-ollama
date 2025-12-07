# resume-analyzer-ollama
AI-powered Resume Analyzer built with Python, Streamlit, and Ollama. Upload your resume (PDF/DOCX/TXT) and ask any questions about it using a local LLM. Completely free, offline, and beginner-friendly prompt engineering project.

Resume Analyzer using Ollama + Streamlit

An AI-powered resume analysis tool that runs completely offline using local LLMs through Ollama.
Upload your resume (PDF/DOCX/TXT) and ask any question — the model answers based only on the resume content.

✨ Features

📄 Upload PDF, DOCX, or TXT resumes

🔍 Automatic text extraction

🤖 Ask any question about your resume

💬 Uses local AI model (via Ollama) — no API key required

⚡ Fast, simple, and beginner-friendly

🔐 Fully offline & free (no OpenAI cost)

🧠 Clean prompt engineering logic

🧠 How It Works

You upload a resume file.

The app extracts text using Python libraries (PyPDF2, python-docx).

Your question + resume text is sent to an offline AI model running in Ollama.

The model responds with accurate answers based only on the resume content.

The UI displays the response in real time.

📁 Project Structure
resume-analyzer-ollama/
│
├── app.py
├── requirements.txt
│
├── services/
│   ├── extractor.py
│   └── llm_client.py
│
└── utils/
    └── prompts.py

🛠️ Tech Stack

Python

Streamlit (UI)

Ollama (local LLMs)

PyPDF2 (PDF extraction)

python-docx (DOCX extraction)

Requests (API communication)

⚙️ Setup Instructions

Follow these steps to run the project locally:

1️⃣ Install Python

Make sure Python 3.9+ is installed.
Check version:

python --version

2️⃣ Create & Activate Virtual Environment
python -m venv venv

Activate on Windows:
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install Ollama

Download from:
https://ollama.com/download

5️⃣ Pull a Model in Ollama

Example (small, fast):

ollama pull llama3.2


Check installed models:

ollama list

6️⃣ Run the App

Start the Streamlit UI:

streamlit run app.py


Your browser will open → Upload resume → Ask questions → Get answers.

🧪 Example Questions You Can Ask

“Summarize this resume.”

“List all skills mentioned in the resume.”

“What projects are included?”

“What improvements should I make?”

“What job roles fit this resume?”

“What questions cannot be answered from the resume?”
