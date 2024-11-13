# Python3 code to demonstrate working of
# Replace all Characters Except K
# Using map() + lambda

# initializing lists
test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']

# printing original list
print("The original list : " + str(test_list))

# initializing repl_chr
repl_chr = '$'

# initializing retain chararter
ret_chr = 'G'

# using map() to extend logic to each element of list
res = list(map(lambda ele: ret_chr if ele == ret_chr else repl_chr, test_list))

# printing result
print("List after replacement : " + str(res))
