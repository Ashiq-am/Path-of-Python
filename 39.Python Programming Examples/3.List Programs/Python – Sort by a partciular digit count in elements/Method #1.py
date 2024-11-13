# Python3 code to demonstrate working of
# Sort by digit count in elements
# Using list comprehension + count() + str()

def count_dig(ele):
    # returning digit count
    return str(ele).count(str(K))


# initializing list
test_list = [4322, 2122, 123, 1344]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# calling external sort
test_list.sort(key=count_dig)

# printing result
print("Sorted list : " + str(test_list))
