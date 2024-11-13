# Python3 code to demonstrate working of
# Toggle i,j elements in List
# Using list comprehension + external function

# external toggle
def toggle(ele, i, j):
    # performing toggle
    if ele == i:
        return j
    elif ele == j:
        return i
    return ele


# initializing list
test_list = [4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4]

# printing original list
print("The original list is : " + str(test_list))

# initializing i, j
i, j = 4, 8

# list comprehension for 1 liner
res = [toggle(ele, i, j) for ele in test_list]

# printing result
print("The altered list : " + str(res))
