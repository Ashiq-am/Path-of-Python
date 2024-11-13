# Python3 code to demonstrate working of
# Check if list is Matix
# using isinstance() + all()

# initialize lists
test_list = [[4, 5], [5, 8], [9, 10]]

# printing original list
print("The original list is : " + str(test_list))

# Check if list is Matix
# using isinstance() + all()
res = all(isinstance(ele, list) for ele in test_list)

# printing result
print("Is list a Matrix ?: " + str(res))
