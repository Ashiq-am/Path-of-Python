# Python program to fetch the indices
# of true values in a Boolean list

# initializing list
bool_list = [False, True, False, True, True, True]

# printing given list
print("Given list is : " + str(bool_list))

# using lambda + filter() + range()
# to return true indices.
res = list(filter(lambda i: bool_list[i], range(len(bool_list))))

# printing result
print("Indices having True values are : " + str(res))
