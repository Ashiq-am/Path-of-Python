# Python3 code to demonstrate working of
# Element Frequency starting with K in dictionary value List
# using loop + startswith()

# initializing dictionary
test_dict = {1: ['Gfg', 'is', 'for', 'Geeks'], 2: ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg', 'best']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 'G'

# Element Frequency starting with K in dictionary value List
# using loop + startswith()
res = 0
for sub in test_dict.values():
    for ele in sub:
        if ele.startswith(K):
            res += 1

# printing result
print("The element frequency starting with K : " + str(res))
