# Program to count the number of each
# vowel in a string

# string of vowels
v = 'aeiou'

# change this value for a different result
str = 'Hello, have you try geeksforgeeks?'

# input from the user
# str = input("Enter a string: ")

# caseless comparisions
str = str.casefold()

# make a dictionary with each vowel a key and value 0
c = {}.fromkeys(v,0)

# count the vowels
for char in str:
		if char in c:
				c[char] += 1
print(c)
