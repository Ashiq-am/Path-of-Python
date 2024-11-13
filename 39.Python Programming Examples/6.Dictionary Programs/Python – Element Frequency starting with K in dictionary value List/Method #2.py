# Python3 code to demonstrate working of
# Element Frequency starting with K in dictionary value List
# using sum() + startswith()

# initializing dictionary
test_dict = {1: ['Gfg', 'is', 'for', 'Geeks'], 2: ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg', 'best']}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = 'G'

# Element Frequency starting with K in dictionary value List
# using sum() + startswith()
res = sum(ele.startswith(K) for ele in [sub for j in test_dict.values() for sub in j])

# printing result
print("The element frequency starting with K : " + str(res))
