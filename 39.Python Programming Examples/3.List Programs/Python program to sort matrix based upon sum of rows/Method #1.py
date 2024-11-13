# Python3 code to demonstrate working of
# Sort Matrix by row sum
# Using sort() + sum()

# helper_fnc
def sum_sort(row):
    # getting sum
    return sum(row)


# initializing list
test_list = [[4, 5], [2, 5, 7], [2, 1], [4, 6, 1]]

# printing original list
print("The original list is : " + str(test_list))

# using sort() to perform sort
test_list.sort(key=sum_sort)

# printing result
print("Sum sorted Matrix : " + str(test_list))
