import json

person = {
    "name": "Nazerke",
    "age": 20,
    "city": "Almaty"
}

# --- PYTHON → JSON STRING ---
json_string = json.dumps(person, indent=4)
print(json_string)

# --- WRITE JSON FILE ---
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

# --- READ JSON FILE ---
with open("person.json", "r") as f:
    data = json.load(f)
print(data)

# --- PARSE JSON STRING ---
text = '{"course":"Python","level":"Beginner"}'
parsed = json.loads(text)
print(parsed)