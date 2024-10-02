import base64
import json
import os
from anthropic import AnthropicVertex

project_id = "optimal-moon-258002"
region = "us-east5"
client = AnthropicVertex(region=region, project_id=project_id)

def get_encoded_image(file_path: str) -> str:
  encoded_image_str = ""
  with open(file_path, "rb") as f:
    encoded_image_str = base64.b64encode(f.read())
  return encoded_image_str.decode("utf-8")

prompt = """
Create JSON from the uploaded image. The first row of the image i
contains the fields. What is the percentage increase from the
slowest mark to the fastest?
"""

file_path = os.path.join("..", "..", "images", "marathon_times.png")

message = client.messages.create(
  max_tokens = 8192,
  messages = [
  {
    "role": "user",
    "content": [
       {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": get_encoded_image(file_path)}},
       {"type": "text", "text": prompt },
    ]
  }],
  model = "claude-3-5-sonnet@20240620",
)

answer = json.loads(message.model_dump_json(indent=2))

print(answer["content"][0]["text"])
