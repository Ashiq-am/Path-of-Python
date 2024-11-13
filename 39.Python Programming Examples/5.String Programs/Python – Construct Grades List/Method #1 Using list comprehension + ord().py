# Python3 code to demonstrate working of
# Construct Grades List
# Using list comprehension + ord()

# initializing N
num = 4

# Using list comprehension + ord()
# each charater paired to symbols and character incremented using idx
# conversion by chr + ord
res = [chr(ord('A') + idx) + sym for idx in range(num)
	for sym in ['+', '', '-']]

# printing result
print("Grades List : " + str(res))
