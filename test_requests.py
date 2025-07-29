import requests

url = "https://www.google.com"

for i in range(30):
    try:
        response = requests.get(url)
        print(f"[{i}] Status: {response.status_code}")
    except Exception as e:
        print("Error:", e)

