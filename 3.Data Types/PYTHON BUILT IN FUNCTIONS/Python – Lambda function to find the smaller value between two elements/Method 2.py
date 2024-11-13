# lambda function to return minimum of two elements
# a, b are the arguments and ternary
# operator is used to compare two elements
get_min = lambda a, b : a if a < b else b

print(get_min(5, 8))
