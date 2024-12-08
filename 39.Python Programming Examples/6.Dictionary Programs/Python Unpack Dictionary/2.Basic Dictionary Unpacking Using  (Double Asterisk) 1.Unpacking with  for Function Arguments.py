def detail(name, age):
    print(name,age)

d = {"name": "Alice", "age": 30}
detail(**d)