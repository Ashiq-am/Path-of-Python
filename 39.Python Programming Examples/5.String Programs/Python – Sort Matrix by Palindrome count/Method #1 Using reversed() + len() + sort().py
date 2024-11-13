# Python3 code to demonstrate working of
# Sort Matrix by Palindrome count
# Using reversed() + len() + sort()

# get palin
def get_palin_freq(row):

	# returning length
	return len([sub for sub in row if ''.join(list(reversed(sub))) == sub])


# initializing list
test_list = [["nitin", "meem", "geeks"], ["peep"],
			["gfg", "is", "best"],
			["sees", "level", "mom", "noon"]]

# printing original list
print("The original list is : " + str(test_list))

# performing sort
test_list.sort(key=get_palin_freq)

# printing result
print("Sorted rows : " + str(test_list))
