# Python3 code to demonstrate working of
# Construct Equidigit tuples
# Using loop + slicing str()

# initializing list
test_list = [5654, 223, 982143, 34, 1021]

# printing original list
print("The original list is : " + str(test_list))

res = []
for sub in test_list:
    # getting mid element
    mid_idx = len(str(sub)) // 2

    # slicing Equidigits
    el1 = str(sub)[:mid_idx]
    el2 = str(sub)[mid_idx:]

    res.append((int(el1), int(el2)))

# printing result
print("Equidigit tuples List : " + str(res))
