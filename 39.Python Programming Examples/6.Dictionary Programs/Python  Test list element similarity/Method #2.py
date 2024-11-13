# Python3 code to demonstrate
# to check whether the list
# K percent same or not
from collections import Counter, defaultdict

# initializing list
ini_list1 = [1, 2, 3, 1, 1, 1, 1, 1, 3, 2]

# printing initial list
print ("Initial list", ini_list1)

# initializing K
K = 60

# code to check whether list is K % same or not
freq = defaultdict(int)
for x in ini_list1:
	freq[x] += 1
freq = freq.values()
if max(freq) >= (K / 100) * sum(freq):
	print ("True")
else:
	print ("False")
