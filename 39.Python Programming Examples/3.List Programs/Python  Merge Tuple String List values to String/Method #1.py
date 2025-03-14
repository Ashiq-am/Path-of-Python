# Python3 code to demonstrate working of
# Merge Tuple String List values to String
# using list comprehension + join()

# initialize list
test_list = [(['g', 'f', 'g'], 1), (['i', 's'], 2), (['b', 'e', 's', 't'], 3)]

# printing original list
print("The original list : " + str(test_list))

# Merge Tuple String List values to String
# using list comprehension + join()
res = [''.join(i) for i, j in test_list]

# printing result
print("The joined character list tuple element to string is : " + str(res))
