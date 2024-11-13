# Python code to find occurrence of any element
# appearing 'n' times

# importing
from collections import defaultdict

# Dictionary declaration
dic = defaultdict(int)

# Input list initialisation
Input = [9, 8, 7, 6, 5, 9, 2]

# Dictionary populate
for i in Input:
	dic[i]+= 1

# constant declaration
n = 2
flag = 0

# Finding from dictionary
for element in Input:
	if element in dic.keys() and dic[element] == n:
		print("Yes, {} has {} occurrence in {}.".format(element, n, Input))
		flag = 1
		break

# if element not found.
if flag == 0:
	print("No occurrences found")
