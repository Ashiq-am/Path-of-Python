# Python3 code to demonstrate working of
# Column Mapped Tuples to dictionary items
# Using dictionary comprehension + zip()

# initializing list
test_list = [[(5, 6), (7, 4), (1, 2)],
             [(7, 3), (10, 14), (11, 22)]]

# printing original list
print("The original list : " + str(test_list))

# nested dictionary comprehension to form pairing
# paired using zip()
res = {key[idx]: val[idx] for key, val in zip(
    *tuple(test_list)) for idx in range(len(key))}

# printing result
print("The constructed dictionary : " + str(res))
