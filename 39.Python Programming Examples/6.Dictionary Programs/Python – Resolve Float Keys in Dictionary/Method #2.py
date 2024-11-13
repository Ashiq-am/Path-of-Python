# Python3 code to demonstrate working of
# Resolve Float Keys in Dictionary
# Using dictionary comprehension + float()

# initializing dictionary
test_dict = {"010.78" : "Gfg", "9.0" : "is", "10" : "Best"}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing K
K = "10.78"

# performing resolution using dictionary comprehension
res = {float(key) : test_dict[key] for key in test_dict}

# converting compare value to float
convK = float(K)

# performing value access
res = res[convK]

# printing result
print("Value of resolved float Key : " + str(res))
