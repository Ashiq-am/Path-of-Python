# Python3 code to demonstrate working of
# Dictionary Keys whose Values summation equals K
# Using loop + update()

# initializing dictionary
test_dict = {"Gfg": 3, "is": 5, "for": 8, "Geeks": 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = "is"

# initializing dictionary to be added
add_item = {"best": 19}

# using dictionary comprehension
res = dict()
for key in test_dict:
    res[key] = test_dict[key]

    # modify after adding K key
    if key == K:
        res.update(add_item)

# printing result
print("Modified dictionary : " + str(res))
