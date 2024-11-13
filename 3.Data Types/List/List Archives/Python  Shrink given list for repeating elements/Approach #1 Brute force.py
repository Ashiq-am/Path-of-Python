# Python3 program to Shrink list
# for repeating elements

def shrinkList(lst):
    tup_list = []
    i, index = 0, 0
    while (index < len(lst)):
        element_count = 0
        while (i < len(lst) and lst[i] == lst[index]):
            element_count += 1
            i += 1
        tup_list.append((lst[index], element_count))
        index += element_count

    return tup_list


# Driver Code
lst = [1, 1, 1, 2, 2, 3, 3, 4]
print(shrinkList(lst))
