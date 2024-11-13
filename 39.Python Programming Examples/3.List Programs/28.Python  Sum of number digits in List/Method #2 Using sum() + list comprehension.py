# Python3 code to demonstrate
# Sum of number digits in List
# using sum() + list comprehension

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using sum() + list comprehension
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))

# printing result
print("List Integer Summation : " + str(res))
