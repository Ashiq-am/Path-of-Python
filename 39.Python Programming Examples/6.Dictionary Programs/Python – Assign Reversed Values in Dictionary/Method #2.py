# Python3 code to demonstrate working of
# Assign Reversed Values in Dictionary
# Using dictionary comprehension + reversed() + values()

# initializing dictionary
test_dict = {1 : "Gfg", 2 : "is", 3 : "Best"}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# extract values using values()
new_val = list(reversed(list(test_dict.values())))

# one-liner dictionary comprehension approach
# enumerate for counter
res = {key : new_val[idx] for idx, key in enumerate(list(test_dict.keys()))}

# printing result
print("Reassigned reverse values : " + str(res))
