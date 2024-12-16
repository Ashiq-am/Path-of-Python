d1 = {1: 10, 2: 20, 3: 30}
# Add new keys where the key is greater than 2
d2 = {k: v * 2 for k, v in d1.items() if k > 2}
print(d2)