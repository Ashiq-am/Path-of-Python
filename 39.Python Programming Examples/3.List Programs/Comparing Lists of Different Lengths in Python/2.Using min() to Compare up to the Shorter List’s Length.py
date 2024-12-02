list1 = [1, 2, 3, 4]
list2 = [10, 20, 30]

for i in range(min(len(list1), len(list2))):
    print(f"{list1[i]} vs {list2[i]}")