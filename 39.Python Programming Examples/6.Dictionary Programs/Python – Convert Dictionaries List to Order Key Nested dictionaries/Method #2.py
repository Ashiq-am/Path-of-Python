# Python3 code to demonstrate working of
# Convert Dictionaries List to Order Key Nested dictionaries
# Using dictionary comprehension + enumerate()

# initializing lists
test_list = [{"Gfg": 3, 4: 9}, {"is": 8, "Good": 2}, {"Best": 10, "CS": 1}]

# printing original list
print("The original list : " + str(test_list))

# dictionary comprehension encapsulating result as one liner
res = {idx: val for idx, val in enumerate(test_list)}

# printing result
print("The constructed dictionary : " + str(res))
