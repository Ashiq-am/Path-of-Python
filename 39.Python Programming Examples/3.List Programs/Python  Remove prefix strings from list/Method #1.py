# Python3 code to demonstrate working of
# Remove prefix strings from list
# using loop + remove() + startswith()

# initialize list
test_list = ['xall', 'xlove', 'gfg', 'xit', 'is', 'best']

# printing original list
print("The original list : " + str(test_list))

# initialize prefix
pref = 'x'

# Remove prefix strings from list
# using loop + remove() + startswith()
for word in test_list[:]:
	if word.startswith(pref):
		test_list.remove(word)

# printing result
print("List after removal of Kth character of each string : " + str(test_list))
