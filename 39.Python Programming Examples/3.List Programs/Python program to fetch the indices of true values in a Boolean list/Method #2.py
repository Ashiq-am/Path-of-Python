# Python program to fetch the indices
# of true values in a Boolean list

# initializing list
bool_list = [False, True, False, True, True, True]

# printing given list
print("Given list is : " + str(bool_list))

# using enumerate() + list comprehension
# to return true indices.
res = [i for i, val in enumerate(bool_list) if val]

# printing result
print("Indices having True values are : " + str(res))
