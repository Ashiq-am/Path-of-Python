# Python3 code to demonstrate working of
# Sort Matrix by None frequency
# Using sort()

# external sort function
def get_None_freq(row):
    # getting length of None characters
    return len([ele for ele in row if not ele])


# initializing list
test_list = [[None, None, 4], [None, None, 3, None],
             [12, 4, 5], [None, 3, 4]]

# printing original list
print("The original list is : " + str(test_list))

# sorting using sort()
test_list.sort(key=get_None_freq)

# printing result
print("List after sorting : " + str(test_list))
