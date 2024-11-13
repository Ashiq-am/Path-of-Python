# Python3 code to demonstrate working of
# Replace tuple according to Nth tuple element
# Using loops + enumerate()

# Initializing list
test_list = [('gfg', 1), ('was', 2), ('best', 3)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing change record
repl_rec = ('is', 2)

# Initializing N
N = 1

# Replace tuple according to Nth tuple element
# Using loops + enumerate()
for key, val in enumerate(test_list):
	if val[N] == repl_rec[N]:
		test_list[key] = repl_rec
		break

# printing result
print("The tuple after replacement is : " + str(test_list))
