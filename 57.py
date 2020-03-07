import json

with open("company1.json", "r") as file:
    d = json.load(file)

print(d)
