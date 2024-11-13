# Python3 code to demonstrate working of
# Maximum length consecutive positive elements
# Using loop

# initializing list
test_list = [4, 5, -4, -1, -7, 2, 5, 6, -2, -9, -10]

# printing original list
print("The original list : " + str(test_list))

# Maximum length consecutive positive elements
# Using loop
counter = 0
max_score = 1
for ele in test_list:
	if ele > 0:
		counter += 1
	else:
		if(counter > 0):
			max_score = max(max_score, counter)
		counter = 0
if(counter > 0):
		max_score = max(max_score, counter)

# printing result
print("Maximum elements run length : " + str(max_score))
