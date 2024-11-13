# Python3 code to demonstrate working of
# Replace tuple according to Nth tuple element
# Using list comprehension

# Initializing list
test_list = [('gfg', 1), ('was', 2), ('best', 3)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing change record
repl_rec = ('is', 2)

# Initializing N
N = 1

# Replace tuple according to Nth tuple element
# Using list comprehension
res = [repl_rec if sub[N] == repl_rec[N] else sub for sub in test_list]

# printing result
print("The tuple after replacement is : " + str(res))
