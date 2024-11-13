""""""



'''
# Python program for the above question

# Function to reorder the characters
#of the string
try : t = int(input())

	# Input test cases
	while t:

		# Input Variables
		n, k = map(int, input().split())
		s = input()
		ans = ""

		# Initialize dictionary
		s_dict = dict()
		for ch in s:
			s_dict[ch] = s_dict.get(ch, 0) + 1
		q = n// k
		a1 = s_dict['1']// q
		a0 = s_dict['0']// q

		# Check for valid conditions
		if(s_dict['1']%2!=0 or s_dict['0']%2!=0 \\
		or s_dict['1']%q!=0 or s_dict['0']%q!=0):
			ans = "Impossible"

		# Otherwise update the result
		else:
			st = ('0'*a0) + ('1'*a1)
			st = ('1'*a1) + ('0'*a0)
			part1 = st + st_rev
			ans = part1*(q// 2)

		# Print the result for the
		# current test case
		print(ans)

		t -= 1

except:
	pass




'''