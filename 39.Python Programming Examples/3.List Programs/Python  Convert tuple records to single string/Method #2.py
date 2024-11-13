# Python3 code to demonstrate working of
# Convert tuple records to single string
# Using map() + join()

# Initializing list
test_list = [('Manjeet', 'Singh'), ('Nikhil', 'Meherwal'), ('Akshat', 'Garg')]

# printing original list
print("The original list is : " + str(test_list))

# Convert tuple records to a single string
# Using map() + join()
res = ', '.join(map(" ".join, test_list))

# printing result
print("The string after tuple conversion: " + res)
