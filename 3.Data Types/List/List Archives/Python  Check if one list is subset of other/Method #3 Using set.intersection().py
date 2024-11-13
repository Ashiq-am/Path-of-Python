# Python3 code to demonstrate
# to check if list is subset of other
# using intersection()

# initializing list
test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5]

# printing original lists
print("Original list : " + str(test_list))
print("Original sub list : " + str(sub_list))

# using intersection() to
# check subset of list
flag = 0
if ((set(sub_list) & set(test_list)) == set(sub_list)):
    flag = 1

# printing result
if (flag):
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")
