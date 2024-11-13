lst = [10, 20, 30, 40, 50]
item = 30
res = [i for i, val in enumerate(lst) if val == item]
if res:
    print(f"The index of {item} in the list is: {res[0]}")
else:
    print(f"{item} is not in the list.")
