d1 = {1: 10, 2: 20, 3: 30}
# Double the values for keys greater than 1
d2 = {k: v * 2 if k > 1 else v for k, v in d1.items()}
print(d2)