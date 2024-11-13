data = [
    ("GeeksforGeeks", "Python", 1000),
    ("GeeksforGeeks", "JavaScript", 1500),
    ("CodingForAll", "Java", 1200),
    ("GeeksforGeeks", "C++", 1300),
    ("CodeWars", "Python", 1100)
]

for tup in data[:]:
    if tup[0] == "GeeksforGeeks":
        data.remove(tup)
print(data)
