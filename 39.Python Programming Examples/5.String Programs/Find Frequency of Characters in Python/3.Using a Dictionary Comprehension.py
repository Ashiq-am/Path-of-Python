s = "GeeksforGeeks"

# Count characters using dictionary comprehension
freq = {c: s.count(c) for c in s}

print(freq)