list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

max_length = max(len(list1), len(list2))

for i in range(max_length):
    item1 = list1[i] if i < len(list1) else None
    item2 = list2[i] if i < len(list2) else None
    print(item1, item2)
