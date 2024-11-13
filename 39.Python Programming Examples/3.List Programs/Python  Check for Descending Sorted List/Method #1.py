# Python3 code to demonstrate
# Check for Descending Sorted List
# using naive method

# initializing list
test_list = [10, 8, 4, 3, 1]

# printing original list
print("Original list : " + str(test_list))

# using naive method to
# Check for Descending Sorted List
flag = 0
i = 1
while i < len(test_list):
    if (test_list[i] > test_list[i - 1]):
        flag = 1
    i += 1

# printing result
if (not flag):
    print("Yes, List is reverse sorted.")
else:
    print("No, List is not reverse sorted.")
