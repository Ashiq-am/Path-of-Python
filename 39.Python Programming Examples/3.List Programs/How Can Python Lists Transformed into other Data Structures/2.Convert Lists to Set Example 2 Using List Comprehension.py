list2 = [1, 2, 2, 3, 3, 3, 'a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c']
set2 = {i for i in list2 if list2.count(i) >= 1}
print(set2)
