lst = [10, 20, 30, 40, 50]
item = 30
res = None
for i in range(len(lst)):
    if lst[i] == item:
        res = i
        break
print(f"The index of {item} in the list is: {res}")
