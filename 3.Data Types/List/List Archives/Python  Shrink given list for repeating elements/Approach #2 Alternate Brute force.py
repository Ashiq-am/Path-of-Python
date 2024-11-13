# Python3 program to Shrink list
# for repeating elements

def shrinkList(lst):
    prev_element = None
    count = 0
    tup_list = []

    for ele in lst:
        if (prev_element == ele):
            count += 1

        elif (prev_element is None):
            count += 1
            prev_element = ele

        else:
            tup_list.append((prev_element, count))
            count = 1
            prev_element = ele

    tup_list.append((prev_element, count))
    return tup_list


# Driver Code
lst = [1, 1, 1, 2, 2, 3, 3, 4]
print(shrinkList(lst))
