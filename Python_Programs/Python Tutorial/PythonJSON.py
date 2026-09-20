import json

name = input("Enter your name: ")
age = int(input("Enter your age: "))
data = {"name": name, "age": age}
json_text = json.dumps(data)
print("JSON:", json_text)
print("Decoded:", json.loads(json_text))
