import PyPDF2
from docx import Document
from io import BytesIO

def extract_pdf(file_bytes):
    reader = PyPDF2.PdfReader(BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_docx(file_bytes):
    doc = Document(BytesIO(file_bytes))
    return "\n".join([p.text for p in doc.paragraphs])

def extract_txt(file_bytes):
    return file_bytes.decode("utf-8")

def extract_text(file):
    name = file.name.lower()
    content = file.read()

    if name.endswith(".pdf"):
        return extract_pdf(content)
    elif name.endswith(".docx"):
        return extract_docx(content)
    elif name.endswith(".txt"):
        return extract_txt(content)
    else:
        return "Unsupported file format."
