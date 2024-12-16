d1 = {1: 10, 2: 20, 3: 30}
# Add items where the key is greater than 2
d2 = {k: v * 2 for k, v in data.items() if k > 2}
print(d2)