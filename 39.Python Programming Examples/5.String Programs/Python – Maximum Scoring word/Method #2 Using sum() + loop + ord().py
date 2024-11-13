# Python3 code to demonstrate working of
# Maximum Scoring word
# Using sum() + loop + ord()
import string

# initializing string
test_str = 'geeks must use geeksforgeeks for cs knowledge'

# printing original string
print("The original string is : " + str(test_str))

score = 0
max_sc = 0
res = ''
for wrd in test_str.split():

	# computing score
	# sum for cummulation
	score = sum(ord(lttr) - 96 for lttr in wrd if lttr in string.ascii_lowercase)

	# updating maximum
	if score > max_sc:
		max_sc = score
		res = wrd

# printing result
print("Maximum scoring word : " + str(res))
