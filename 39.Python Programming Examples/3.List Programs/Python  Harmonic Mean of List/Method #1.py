# Python3 code to demonstrate working of
# Harmonic Mean of List
# using loop + formula

# initialize list
test_list = [6, 7, 3, 9, 10, 15]

# printing original list
print("The original list is : " + str(test_list))

# Harmonic Mean of List
# using loop + formula
sum = 0
for ele in test_list:
	sum += 1 / ele
res = len(test_list)/sum

# printing result
print("The harmonic mean of list is : " + str(res))
