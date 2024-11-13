def merge(list1, list2):
    merged_list = []
    for i in range(max((len(list1), len(list2)))):

        while True:
            try:
                tup = (list1[i], list2[i])
            except IndexError:
                if len(list1) > len(list2):
                    list2.append('')
                    tup = (list1[i], list2[i])
                elif len(list1) < len(list2):
                    list1.append('')
                    tup = (list1[i], list2[i])
                continue

            merged_list.append(tup)
            break
    return merged_list


# Driver code
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))
