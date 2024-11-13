# Python3 program to Find
# longest K words in a list
from itertools import count

def longest_word(lst, K):
	cnt = count()
	return sorted(lst, key = lambda w : (len(w), next(cnt)),
										reverse = True)[:K]

# Driver code
lst = ['am', 'watermelon', 'girl', 'boy', 'colour']
K = 3
print(longest_word(lst, K))
