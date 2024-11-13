# Python3 code to demonstrate working of
# String construction from character frequency
# using join() + list comprehension

# initialize list
test_list = [('g', 4), ('f', 3), ('g', 2)]

# printing original list
print("The original list : " + str(test_list))

# String construction from character frequency
# using join() + list comprehension
res = ''.join(char * freq for char, freq in test_list)

# printing result
print("The constructed string is : " + str(res))
