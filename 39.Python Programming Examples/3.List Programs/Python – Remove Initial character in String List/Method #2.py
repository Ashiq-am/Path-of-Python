# Python3 code to demonstrate
# Remove Initial character in String List
# using map() + lambda

# initializing list
test_list = ['Amanjeet', 'sakash', 'kakshat', 'Knikhil']

# printing original list
print("The original list : " + str(test_list))

# using map() + lambda
# Remove Initial character in String List
res = list(map(lambda i: i[ 1 : ], test_list))

# printing result
print("The list after removing initial characters : " + str(res))
