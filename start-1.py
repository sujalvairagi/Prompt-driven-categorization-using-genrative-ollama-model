import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "llava:7b",
    "prompt": "tell me a short happy story",
    "stream": True
}

response = requests.post(url, json=data, stream=True)

if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode("utf-8")
            json_data = json.loads(decoded_line)
            print(json_data.get("response", ""), end="", flush=True)
else:
    print("Request failed with status code:", response.status_code)
