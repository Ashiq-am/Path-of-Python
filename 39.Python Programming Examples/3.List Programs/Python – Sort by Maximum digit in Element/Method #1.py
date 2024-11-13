# Python3 code to demonstrate working of
# Sort by Maximum digit in Element
# Using max() + sort()

def max_dig(ele):
    # getting maximum digit by magnitude
    return max(str(ele))


# initializing list
test_list = [234, 92, 15, 8, 721]

# printing original list
print("The original list is : " + str(test_list))

# calling sort fnc. to sort with key
test_list.sort(key=max_dig)

# printing result
print("Sorted List : " + str(test_list))
