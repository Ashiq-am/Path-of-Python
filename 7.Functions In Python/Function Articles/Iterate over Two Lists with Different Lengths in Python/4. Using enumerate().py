list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']

# iterate over the longer list (list2)
for i, _ in enumerate(list2):
    elem1 = list1[i] if i < len(list1) else None
    elem2 = list2[i]
    print(elem1, elem2)
