# Python code to implement the above approach

# Structure of a trie node
class Trie:
	def __init__(self):
		self.cnt = 0
		self.ch = [None] * 26

# Function to build the trie
def build(a, root):
	temp = None
	for i in range(len(a)):
		temp = root
		for j in range(len(a[i])):
			if not temp.ch[ord(a[i][j]) - ord('a')]:
				temp.ch[ord(a[i][j]) - ord('a')] = Trie()
			temp.ch[ord(a[i][j]) - ord('a')].cnt += 1
			temp = temp.ch[ord(a[i][j]) - ord('a')]

# Function to find a string in the trie
def find(s, root):
	for i in range(len(s)):
		if not root.ch[ord(s[i]) - ord('a')]:
			return 0
		root = root.ch[ord(s[i]) - ord('a')]
	return root.cnt

# Function to get the given number of string
# having the same prefix as the query
def prefixCount(N, Q, list, query):
	res = []
	root = Trie()
	build(list, root)
	for i in range(Q):
		res.append(find(query[i], root))
	return res

# Driver Code
words = ["geekf", "geeks", "geeksforgeeks","string", "strong"]
queries = ["geek", "gel", "str"]

# Function call
ans = prefixCount(len(words), len(queries), words, queries)

print(ans)
