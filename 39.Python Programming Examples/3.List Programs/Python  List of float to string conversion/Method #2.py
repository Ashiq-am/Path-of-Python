# Python3 code to demonstrate working of
# List of float to string conversion
# using join() + map() + str()

# initialize list
test_list = [5.8, 9.6, 10.2, 45.3, 6.0]

# printing original list
print("The original list is : " + str(test_list))

# Convert float list to string
# using join() + map() + str()
res1 = " ".join(str(test_list))

# List of float to string conversion
# using join() + map() + str()
res2 = " ".join(map(str, test_list))

# printing result
print("Conversion using join + str : " + str(res1))
print("Conversion using join + str + map : " + str(res2))
