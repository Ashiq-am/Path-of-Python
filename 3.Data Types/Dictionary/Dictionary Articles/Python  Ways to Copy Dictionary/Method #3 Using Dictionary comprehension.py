# Python3 code to demonstrate
# how to copy dictionary
# using dictionary comprehension


# initialising dictionary
test1 = {"name" : "akshat", "name1" : "manjeet", "name2" : "vashu"}


# method to copy dictionary using dictionary comprehension
test2 = {k:v for k, v in test1.items()}


# updating test2
test2["name1"] ="ayush"

# print initial dictionary
print("initial dictionary = ", test1)

# printing updated dictionary
print("updated dictionary = ", test2)
