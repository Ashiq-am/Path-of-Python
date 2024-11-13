# Python3 code to demonstrate working of
# Unique values count of each Key
# Using len() + set()

# initializing lists
test_list = [{"gfg": 1, "is": 3, "best": 2}, {
	"gfg": 1, "is": 3, "best": 6}, {"gfg": 7, "is": 3, "best": 10}]

# printing original list
print("The original list is : " + str(test_list))

res = dict()
for key in test_list[0].keys():

	# mapping unique values.
	res[key] = len(set([sub[key] for sub in test_list]))

# printing result
print("Unique count of keys : " + str(res))
