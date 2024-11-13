# Python3 code to demonstrate working of
# K Maximum elements with Index in List
# Using sorted() + index()

# initializing list
test_list = [5, 3, 1, 4, 7, 8, 2]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 3

# Using sorted() + index()
# using sorted() to sort and slice K maximum elements
temp = sorted(test_list)[-K:]
res = []
for ele in temp:
    # encapsulating elements with index using index()
    res.append((test_list.index(ele), ele))

# printing result
print("K Maximum with indices : " + str(res))
