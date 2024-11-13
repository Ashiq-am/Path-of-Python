# Python3 program to Find
# longest K words in a list
import heapq
from operator import itemgetter

def longest_word(lst, K):
	# constructing heap
	heap = [(0, i, '') for i in range(K)]
	heapq.heapify(heap)

	# To maintain top K elements
	for i, word in enumerate(lst):
		item = (len(word), i, word)
		if item > heap[0]:
			heapq.heapreplace(heap, item)

	return sorted(list(map(itemgetter(2), heap)),
							key = len, reverse = True)


# Driver code
lst = ['am', 'watermelon', 'girl', 'boy', 'colour']
K = 3
print(longest_word(lst, K))
