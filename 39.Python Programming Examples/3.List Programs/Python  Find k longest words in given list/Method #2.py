# Python3 program to Find
# longest K words in a list

def longest_word(lst, K):
	idx, words = zip(*sorted(enumerate(lst),
	key = lambda w: (-len(w[1]), -w[0]))[:K])
	return list(words)

# Driver code
lst = ['am', 'watermelon', 'girl', 'boy', 'colour']
K = 3
print(longest_word(lst, K))
