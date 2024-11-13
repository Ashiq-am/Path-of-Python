# Python3 code to demonstrate
# Check for Descending Sorted List
# using sort() + reverse

# initializing list
test_list = [10, 5, 4, 3, 1]

# printing original list
print("Original list : " + str(test_list))

# using sort() + reverse to
# Check for Descending Sorted List
flag = 0
test_list1 = test_list[:]
test_list1.sort(reverse=True)
if (test_list1 == test_list):
    flag = 1

# printing result
if (flag):
    print("Yes, List is reverse sorted.")
else:
    print("No, List is not reverse sorted.")
