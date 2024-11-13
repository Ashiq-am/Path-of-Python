# Python3 code to demonstrate working of
# Type conversion in Nested and Mixed List
# Using recursion + isinstance()

# helper_fnc
def change_type(sub):
    if isinstance(sub, list):
        return [change_type(ele) for ele in sub]
    elif isinstance(sub, tuple):
        return tuple(change_type(ele) for ele in sub)
    else:
        return int(sub)


# initializing list
test_list = ['6', '89', ('7', ['8', '10']), ['11', '15']]

# printing original list
print("The original list is : " + str(test_list))

# Type conversion in Nested and Mixed List
# Using recursion + isinstance()
res = change_type(test_list)

# printing result
print("Data after type conversion : " + str(res))
