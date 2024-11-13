# Python3 code to demonstrate working of
# Convert List to Index and Value dictionary
# Using loop + enumerate()

# initializing list
test_list = [3, 5, 7, 8, 2, 4, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing keys for index and vals
idx, val = "indx", "vals"

# initializing empty mesh
res = {idx: [], val: []}
for id, vl in enumerate(test_list):
    res[idx].append(id)
    res[val].append(vl)

# printing results
print("Constructed dictionary : " + str(res))
