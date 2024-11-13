# Python3 code to demonstrate working of
# Count of Matching i, j index elements
# Using loop

# initialize list
test_list = ['geeks', 'beke', 'treat', 'neke']

# printing original list
print("The original list : " + str(test_list))

# initialize i
i = 1

# initialize j
j = 3

# Count of Matching i, j index elements
# Using loop
count = 0
for ele in test_list:
	if ele[i] == ele[j]:
		count = count + 1

# printing result
print("Total Strings with similar ith and jth elements : " + str(count))
