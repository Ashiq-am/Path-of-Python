# Python3 code to demonstrate working of
# Conditional Join Dictionary List
# Using update() + next()

# initializing lists
test_list1 = [{"gfg": 1, "is": 3, "best": 2}, {
	"gfg": 1, "best": 6}, {"all": 7, "best": 10}]
test_list2 = [{"good": 4, "best": 2}, {
	"geeks": 2, "best": 3}, {"CS": 2, "best": 10}]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing test key
test_key = "best"

for sub1 in test_list1:

	# checking for matching key
	temp = next(
		(itm for itm in test_list2 if sub1[test_key] == itm[test_key]), None)
	if(temp):

		# performing update
		sub1.update(temp)

# printing result
print("Joined result : " + str(test_list1))
