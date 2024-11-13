# Python3 code to demonstrate working of
# Check if previous element is smaller in List
# Using zip() + list comprehension

# initializing list
test_list = [6, 3, 7, 3, 6, 7, 8, 3]

# printing original list
print("The original list is : " + str(test_list))

# Check if previous element is smaller in List
# Using zip() + list comprehension
res = [int(sub1) < int(sub2) for sub1, sub2 in zip(test_list, test_list[1:])]

# printing result
print("List after filtering : " + str(res))
