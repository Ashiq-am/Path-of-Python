# Python3 code to demonstrate working of
# Group concatenate Till K
# Using loop + join() + list comprehension

# initializing lists
test_list = ["Gfg", "is", "Best", None, "I", "Love", None, "Gfg"]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = None

# all() to encapsulate whole logic into one expression
res = [[]]
for sub in test_list:

    # checking for K value, and performing append to
    # latest list
    if sub != K:
        res[-1].append(sub)
    else:

        # constructing new list if new group
        res.append([])

    # Joining all groups
fin_res = [' '.join(ele) for ele in res]

# printing result
print("Concatenated Groups : " + str(fin_res))
