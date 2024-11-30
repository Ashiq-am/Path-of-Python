# Removing multiple characters using translate()

s1 = "Welcome to Python programming!"
ch = "om "

a = str.maketrans("", "", ch)
s2 = s1.translate(a)

print(s2)