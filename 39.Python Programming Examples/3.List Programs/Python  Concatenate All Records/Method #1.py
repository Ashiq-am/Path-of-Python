# Python3 code to demonstrate working of
# Concatenate All Records
# using join() + generator expression

# initialize list
test_list = [('geeksforgeeks ', 'is' ), (' best', ' for'), (' all', ' geeks')]

# printing original list
print("The original list : " + str(test_list))

# Concatenate All Records
# using join() + generator expression
res = "".join(j for i in test_list for j in i)

# printing result
print("The Concatenated elements of list is : " + res)
