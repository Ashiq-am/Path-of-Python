# Using lambda function we first convert all
# the cell to a string value and then find
# its length using len() function
df.applymap(lambda x: len(str(x)))
