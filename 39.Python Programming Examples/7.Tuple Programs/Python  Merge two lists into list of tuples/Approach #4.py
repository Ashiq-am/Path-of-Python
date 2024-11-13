def merge(list1, list2):
    merged_list = [(p1, p2) for idx1, p1 in enumerate(list1)
                   for idx2, p2 in enumerate(list2) if idx1 == idx2]
    return merged_list


# Driver code
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))
