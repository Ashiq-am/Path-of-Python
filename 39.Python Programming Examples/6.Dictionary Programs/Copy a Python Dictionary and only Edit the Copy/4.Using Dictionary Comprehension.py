# Using dictionary comprehension
test1 = {"1": "one", "2": "two", "3": "three"}
test2 = {key: value for key, value in test1.items()}
test2["2"] = "five"

# Printing the initial dictionary 'test1'
print("Initial Dictionary:", test1)

# Printing the updated dictionary 'test2'
print("Updated Dictionary:", test2)
