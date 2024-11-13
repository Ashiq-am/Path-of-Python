# Python3 code to demonstrate working of
# Filter unique valued tuples
# Using loop + set()

# initializing list
test_list = [(3, 5, 6, 7), (3, 2, 4, 3), (9, 4), (2, 3, 2)]

# printing original list
print("The original list is : " + str(test_list))

res = []

for sub in test_list:

    # checking lengths to be equal
    if len(set(sub)) == len(sub):
        res.append(sub)

# printing results
print("Filtered tuples : " + str(res))
