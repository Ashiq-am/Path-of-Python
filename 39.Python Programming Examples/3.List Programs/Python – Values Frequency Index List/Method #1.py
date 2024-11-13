# Python3 code to demonstrate working of
# Values Frequency Index List
# Using loop

# initializing list
test_list = [('Gfg', 3), ('is', 3), ('best', 1), ('for', 5), ('geeks', 1)]

# printing original list
print("The original list is : " + str(test_list))

# Values Frequency Index List
# Using loop
res = [0 for _ in range(6)]
for ele in test_list:
	res[ele[1]] = res[ele[1]] + 1

# printing result
print("The Frequency list : " + str(res))
