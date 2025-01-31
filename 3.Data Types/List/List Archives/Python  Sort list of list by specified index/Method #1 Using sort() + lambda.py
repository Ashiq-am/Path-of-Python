# Python 3 code to demonstrate
# to sort list of list by given index
# using sort() + lambda


# initializing list
test_list = [['Rash', 4, 28], ['Varsha', 2, 20], ['Nikhil', 1, 20], ['Akshat', 3, 21]]

# printing original list
print ("The original list is : " + str(test_list))

# using sort() + lambda
# to sort list of list
# sort by second index
test_list.sort(key = lambda test_list: test_list[1])

# printing result
print ("List after sorting by 2nd element of lists : " + str(test_list))
