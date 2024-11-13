numbers = [10, 20, 30, 40, 50]
target = 35

for num in numbers:
    if num == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found in the list.")
