from string import ascii_lowercase

# function to compute frequencies


def get_freq(test_str):

	# starting at 0 count
	freqs = {char: 0 for char in ascii_lowercase}

	# counting frequencies
	for char in test_str:
		freqs[char] += 1
	return freqs


# initializing strings
test_str1 = 'aabcdaa'
test_str2 = "abbaccd"

# printing original strings
print("The original string 1 is : " + str(test_str1))
print("The original string 2 is : " + str(test_str2))

# initializing K
K = 2

# getting frequencies
freqs_1 = get_freq(test_str1)
freqs_2 = get_freq(test_str2)

# checking for frequencies
res = True
for char in ascii_lowercase:
	if abs(freqs_1[char] - freqs_2[char]) > K:
		res = False
		break

# printing result
print("Are strings similar ? : " + str(res))
