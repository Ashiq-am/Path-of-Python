# Python3 code to demonstrate
# to check whether the list
# K percent same or not
from collections import Counter

# initializing list
ini_list1 = [1, 2, 3, 1, 1, 1, 1, 1, 3, 2]

# printing initial list
print ("Initial list", ini_list1)

# initializing K
K = 60

# code to check whether list is K % same or not
i, freq = Counter(ini_list1).most_common(1)[0]

if len(ini_list1)*(K / 100) <= freq:
	print("True")
else:
	print("False")
