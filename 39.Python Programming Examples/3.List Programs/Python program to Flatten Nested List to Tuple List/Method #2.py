# Python3 code to demonstrate working of
# Multiflatten Tuple List
# Using yield + recursion

def remove_lists(test_list):
    if isinstance(test_list, list):

        # return intermediate to recursive function
        for ele in test_list:
            yield from remove_lists(ele)
    else:
        yield test_list


# initializing list
test_list = [[[(4, 6)]], [[[(7, 4)]]], [[[[(10, 3)]]]]]

# printing original list
print("The original list is : " + str(test_list))

# calling recursive function
res = list(remove_lists(test_list))

# printing result
print("The Flattened container : " + str(res))
