# Python3 program for above approach

# Function to calculate Roman values
def intToRoman(num):

	# Storing roman values of digits from 0-9
	# when placed at different places
	m = ["", "M", "MM", "MMM"]
	c = ["", "C", "CC", "CCC", "CD", "D",
		"DC", "DCC", "DCCC", "CM "]
	x = ["", "X", "XX", "XXX", "XL", "L",
		"LX", "LXX", "LXXX", "XC"]
	i = ["", "I", "II", "III", "IV", "V",
		"VI", "VII", "VIII", "IX"]

	# Converting to roman
	thousands = m[num // 1000]
	hundereds = c[(num % 1000) // 100]
	tens = x[(num % 100) // 10]
	ones = i[num % 10]

	ans = (thousands + hundereds +
		tens + ones)

	return ans

# Driver code
if __name__ == "__main__":
	number = 3549
	print(intToRoman(number))
