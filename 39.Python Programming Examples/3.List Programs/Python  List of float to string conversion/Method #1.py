# Python3 code to demonstrate working of
# List of float to string conversion
# using list comprehension + str() + join()

# initialize list
test_list = [5.8, 9.6, 10.2, 45.3, 6.0]

# printing original list
print("The original list is : " + str(test_list))

# List of float to string conversion
# using list comprehension + str() + join()
res = " ".join([str(i) for i in test_list])

# printing result
print("Conversion of float list to string : " + str(res))
