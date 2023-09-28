import requests

url = "http://localhost:5000/chat"

# User input
user_input = input("Ask AI:")

# Send a POST request with an increased timeout (e.g., 30 seconds)
data = {"user_input": user_input}
response = requests.post(url, json=data, timeout=30)

# Handle the response as needed
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