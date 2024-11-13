# Python3 code to demonstrate working of
# Accessing variable value from code scope
# using locals

# initialize variable
test_var = "gfg is best"

# printing original variable
print("The original variable : " + str(test_var))

# Accessing variable value from code scope
# using locals
res = locals()['test_var']

# printing result
print("Variable accessed using dictionary : " + str(res))
