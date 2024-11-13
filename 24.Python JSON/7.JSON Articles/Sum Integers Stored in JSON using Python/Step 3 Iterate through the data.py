sum = 0
for key, val in data.items():
    if isinstance(val, int):
        sum += val
