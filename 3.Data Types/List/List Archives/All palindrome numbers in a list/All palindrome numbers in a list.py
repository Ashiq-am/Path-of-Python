# Python program to count and
# print all palindrome numbers in a list.

def palindromeNumbers(list_a):

	c = 0

	# loop till list is not empty
	for i in list_a:

		# Find reverse of current number
		t = i
		rev = 0
		while t > 0:
			rev = rev * 10 + t % 10
			t = t // 10

		# compare rev with the current number
		if rev == i:
			print (i)
			c = c + 1

	print()
	print ("Total palindrome nos. are", c )
	print()

# Driver code
def main():

	list_a = [10, 121, 133, 155, 141, 252]
	palindromeNumbers(list_a)

	list_b = [ 111, 220, 784, 565, 498, 787, 363]
	palindromeNumbers(list_b)

if __name__=="__main__":
	main()		 # main function call
