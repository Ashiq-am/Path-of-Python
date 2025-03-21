# Python3 code to demonstrate working of
# Convert Matrix to String
# Using map() + join()

# initializing list
test_list = [[1, 3, "gfg"], [2, "is", 4], ["best", 9, 5]]

# printing original list
print("The original list is : " + str(test_list))

# initializing delims
in_del, out_del = ",", " "

# nested join using join()
# map() for joining inner elements
res = out_del.join(in_del.join(map(str, sub)) for sub in test_list)

# printing result
print("Conversion to String : " + str(res))
