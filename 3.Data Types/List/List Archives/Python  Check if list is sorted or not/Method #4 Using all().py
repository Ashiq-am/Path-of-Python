# Python3 code to demonstrate
# to check if list is sorted
# using all()

# initializing list
test_list = [9, 4, 5, 8, 10]

# printing original list
print("Original list : " + str(test_list))

# using all() to
# check sorted list
flag = 0
if (all(test_list[i] <= test_list[i + 1] for i in range(len(test_list) - 1))):
    flag = 1

# printing result
if (flag):
    print("Yes, List is sorted.")
else:
    print("No, List is not sorted.")
