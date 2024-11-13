# Python code to demonstrate
# return the sum of values of dictionary
# with same keys in list of dictionary

from collections import deque

# Initialising list of dictionary
ini_lis1 = ['a', 'b', 'c', 'd', 'e']
ini_lis2 = deque([1, 2, 3])

# zipping in cyclic if shorter length
result = {}
for letter in ini_lis1:
	number = ini_lis2.popleft()
	result[letter] = number
	ini_lis2.append(number)

print("resultant dictionary : ", str(result))
