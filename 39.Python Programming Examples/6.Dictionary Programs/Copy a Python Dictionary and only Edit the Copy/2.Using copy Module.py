from copy import deepcopy

test1 = {"1" : "one", "2" : "t0w", "3" : "three"}
test2 = deepcopy(test1)
test2["2"] = "two"

# print initial dictionary
print("initial dictionary = ", test1)

# printing updated dictionary
print("updated dictionary = ", test2)
