import requests

url = "http://localhost:5000/chat"

user_input = input("Ask AI:")

data = {"user_input": user_input}
response = requests.post(url, json=data, timeout=30)

if response.status_code == 200:
    ai_response = response.json().get("AI")
    if ai_response:
        print("AI Response:")
        for text in ai_response:
            print(text)
    else:
        print("No AI response received.")
else:
    print("Error:", response.status_code)
