# Python3 code to demonstrate
# how to copy dictionary
# using copy() function


# initialising dictionary
test1 = {"name" : "akshat", "name1" : "manjeet", "name2" : "vashu"}


# method to copy dictionary using copy() function
test2 = test1.copy()


# updating test2
test2["name1"] ="nikhil"

# print initial dictionary
print("initial dictionary = ", test1)

# printing updated dictionary
print("updated dictionary = ", test2)
