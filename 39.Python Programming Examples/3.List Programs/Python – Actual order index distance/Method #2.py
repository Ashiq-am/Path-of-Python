# Python3 code to demonstrate
# Actual order index distance
# using map() + enumerate() + dictionary comprehension + sorted()

# initializing list
test_list = [6, 3, 1, 2, 5, 4]

# printing original list
print("The original list is : " + str(test_list))

# using map() + enumerate() + dictionary comprehension + sorted()
# Actual order index distance
temp = {val: abs(key - test_list.index(val)) for key, val in enumerate(sorted(test_list))}
res = list(map(temp.get, test_list))

# printing result
print ("The relative ordering list is : " + str(res))
