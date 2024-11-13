# Python3 code to demonstrate working of
# Index Value repetition in List
# Using list comprehension + enumerate()

# initializing Matrix
test_list = [3, 0, 4, 2]

# printing original list
print("The original list is : " + str(test_list))

# enumerate() gets index and value of similar index element
res = [ele for sub in ([idx] * ele for idx,
                                       ele in enumerate(test_list)) for ele in sub]

# printing result
print("Constructed List : " + str(res))
