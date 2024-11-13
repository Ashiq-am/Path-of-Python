# Python3 code to demonstrate working of
# Sort Matrix by Palindrome count
# Using sorted() + len() + reversed()

# initializing list
test_list = [["nitin", "meem", "geeks"], ["peep"],
			["gfg", "is", "best"], ["sees", "level", "mom", "noon"]]

# printing original list
print("The original list is : " + str(test_list))

# performing sort
# sorted() and lambda used to get 1 sentence approach
res = sorted(test_list, key=lambda row: len(
	[sub for sub in row if ''.join(list(reversed(sub))) == sub]))

# printing result
print("Sorted rows : " + str(res))
