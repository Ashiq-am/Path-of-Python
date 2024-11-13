# Python3 code to demonstrate working of
# Multiflatten Tuple List
# Using recursion + isinstance()


res = []


def remove_lists(test_list):
    for ele in test_list:

        # checking for wrapped list
        if isinstance(ele, list):
            remove_lists(ele)
        else:
            res.append(ele)
    return res


# initializing list
test_list = [[[(4, 6)]], [[[(7, 4)]]], [[[[(10, 3)]]]]]

# printing original list
print("The original list is : " + str(test_list))

# calling recursive function
res = remove_lists(test_list)

# printing result
print("The Flattened container : " + str(res))
