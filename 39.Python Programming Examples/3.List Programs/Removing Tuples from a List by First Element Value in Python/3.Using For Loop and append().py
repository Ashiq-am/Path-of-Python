data = [
    ("GeeksforGeeks", "Python", 1000),
    ("GeeksforGeeks", "JavaScript", 1500),
    ("CodingForAll", "Java", 1200),
    ("GeeksforGeeks", "C++", 1300),
    ("CodeWars", "Python", 1100)
]

# new list
new_data = []
for tup in data[:]:
    if tup[0] != "GeeksforGeeks":
        new_data.append(tup)
print(new_data)
