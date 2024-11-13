# Python3 code to demonstrate working of
# Convert tuple records to single string
# Using list comprehension + join()

# Initializing list
test_list = [('Manjeet', 'Singh'), ('Nikhil', 'Meherwal'), ('Akshat', 'Garg')]

# printing original list
print("The original list is : " + str(test_list))

# Convert tuple records to a single string
# Using list comprehension + join()
res = ', '.join([' '.join(sub) for sub in test_list])

# printing result
print("The string after tuple conversion: " + res)
