data = [
    ("GeeksforGeeks", "Python", 1000),
    ("GeeksforGeeks", "JavaScript", 1500),
    ("CodingForAll", "Java", 1200),
    ("GeeksforGeeks", "C++", 1300),
    ("CodeWars", "Python", 1100)
]

data = list(filter(lambda x: x[0] != "GeeksforGeeks", data))
print(data)
