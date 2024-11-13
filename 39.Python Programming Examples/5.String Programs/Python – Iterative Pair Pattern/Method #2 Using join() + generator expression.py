# Python3 code to demonstrate working of
# Iterative Pair Pattern
# Using join() + generator expression

# initializing 1st element
frst_ele = 'G'

# initializing 2nd element
secnd_ele = '*'

# initializing N
N = 4

# Iterative Pair Pattern
# Using join() + generator expression
res = frst_ele.join(secnd_ele * idx for idx in range(N + 1))

# printing result
print("The constructed pattern is : " + str(res))
