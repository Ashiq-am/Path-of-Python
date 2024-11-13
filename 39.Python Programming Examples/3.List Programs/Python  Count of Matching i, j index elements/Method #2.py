# Python3 code to demonstrate working of
# Count of Matching i, j index elements
# Using sum() + generator expression

# initialize list
test_list = ['geeks', 'beke', 'treat', 'neke']

# printing original list
print("The original list : " + str(test_list))

# initialize i
i = 1

# initialize j
j = 3

# Count of Matching i, j index elements
# Using sum() + generator expression
res = sum(1 for ele in test_list if ele[i] == ele[j])

# printing result
print("Total Strings with similar ith and jth elements : " + str(res))
