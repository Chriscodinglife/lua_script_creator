import requests

url = "http://127.0.0.1:8000/convert"

with open("test.png", "rb") as image_file:
    image_data = image_file.read()

payload={}
files=[
  ('file',('test.png',image_data,'image/png'))
]
headers = {}

response = requests.request("POST", url, headers=headers, files=files)

print(response.text)
