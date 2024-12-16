d = {1: 10, 2: 20, 3: 30}
for i in range(4, 6):  # Add keys dynamically
    d[i] = i * 10  # Assign a value based on the key
print(d)