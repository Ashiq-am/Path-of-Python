# Python3 code to demonstrate working of
# Maximum Scoring word
# Using split() + loop + ord() + ascii_lowercase
import string

# initializing string
test_str = 'geeks must use geeksforgeeks for cs knowledge'

# printing original string
print("The original string is : " + str(test_str))

score = 0
max_sc = 0
res = ''
for wrd in test_str.split():
	score = 0
	# computing score
	for lttr in wrd:
		if lttr in string.ascii_lowercase:
			score += ord(lttr) - 96

	# updating maximum
	if score > max_sc:
		max_sc = score
		res = wrd

# printing result
print("Maximum scoring word : " + str(res))
