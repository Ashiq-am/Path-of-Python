d1 = {'a': 1, 'b': 2, 'c': 3}

# Reverse the dictionary using dictionary comprehension
d2 = {v: k for k, v in d1.items()}

print(d2)