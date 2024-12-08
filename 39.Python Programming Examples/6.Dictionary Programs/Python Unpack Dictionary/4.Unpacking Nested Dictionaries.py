dict = {"p1": {"name": "Alice", "age": 30}}
for person, info in dict.items():
    name, age = info["name"], info["age"]
    print(person, name, age)