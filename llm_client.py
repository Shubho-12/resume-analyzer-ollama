import requests

def call_ollama(prompt, model="llama3.2"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json().get("response", "")
