# Removing multiple characters using str.replace()

s = "Welcome to Python programming!"
ch = ['o', 'm', ' ']

for i in ch:
    s = s.replace(i, "")

print(s)
