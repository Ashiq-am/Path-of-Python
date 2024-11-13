# Python3 code to demonstrate working of
# Columns to Dictionary Conversion in Matrix
# Using dictionary comprehension + zip()

# initializing list
test_list = [[4, 5, 7], [10, 8, 3], [19, 4, 6], [9, 3, 6]]

# printing original list
print("The original list : " + str(test_list))

# appropriate slicing before zip function
res = {ele[0]: list(ele[1:]) for ele in zip(*test_list)}

# printing result
print("Reformed dictionary : " + str(res))
