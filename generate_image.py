import json
import requests
import uuid

SERVER = "http://127.0.0.1:8188"


# prompt load
with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt_text = f.read()

print("PROMPT LOADED:\n")
print(prompt_text)


# workflow load
with open("workflow_api.json", "r", encoding="utf-8") as f:
    workflow = json.load(f)


# positive prompt replace
workflow["20:6"]["inputs"]["text"] = prompt_text


payload = {
    "prompt": workflow,
    "client_id": str(uuid.uuid4())
}

response = requests.post(
    f"{SERVER}/prompt",
    json=payload
)

print(response.json())