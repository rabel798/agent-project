import requests
def call_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()

    return result["candidates"][0]["content"]["parts"][0]["text"]

#this takes a task as input and breaks it down into clear steps using the Gemini API