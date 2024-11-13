# Python3 code to demonstrate
# append from front and remove from rear
# using + operator and list slicing

# initializing list
test_list = [4, 5, 7, 3, 10]

# printing original list
print("The original list : " + str(test_list))

# using + operator and list slicing
# append from front and remove from rear
res = [13] + test_list[:-1]

# printing result
print("The list after append and removal : " + str(res))
