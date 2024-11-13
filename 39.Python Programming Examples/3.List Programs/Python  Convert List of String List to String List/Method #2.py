# Python3 code to demonstrate working of
# Convert List of String List to String List
# using eval() + list comprehension

# initialize list
test_list = ["[1, 4]", "[5, 6]", "[7, 10]"]

# printing original list
print("The original list : " + str(test_list))

# Convert List of String List to String List
# using eval() + list comprehension
res = [''.join(str(b) for b in eval(a)) for a in test_list]

# printing result
print("List after performing conversion : " + str(res))
