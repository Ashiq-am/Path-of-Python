class Node:
	def __init__(self):
		# Array to store child nodes for each letter of the alphabet
		self.children = [None] * 26
		# Flag to indicate the end of a word
		self.eow = False


def insert(root, s):
	# Function to insert a word into the trie
	curr = root
	for c in s:
		# Calculate the index corresponding to the current character
		idx = ord(c) - ord('a')
		# If the child node for the current character does not exist, create one
		if curr.children[idx] is None:
			curr.children[idx] = Node()
		# Move to the child node
		curr = curr.children[idx]
	# Mark the end of the word
	curr.eow = True


def longest_string_with_all_prefix(root, pre):
	# Function to find the longest string with a given prefix in the trie
	if root is None:
		return pre
	# Initialize the longest string with the given prefix
	longest = pre
	for i in range(26):
		# Iterate through the child nodes
		if root.children[i] is not None and root.children[i].eow:
			# If a valid word is found, recursively find the longest string with the updated prefix
			s = pre + chr(i + ord('a'))
			curr = longest_string_with_all_prefix(root.children[i], s)
			# Update the longest string if the current one is longer
			if len(curr) > len(longest):
				longest = curr
	return longest


if __name__ == "__main__":
	# Create the root node of the trie
	root = Node()
	# List of words to insert into the trie
	words = ["apply", "apple", "a", "ap", "app", "appl", "banana"]
	# Insert each word into the trie
	for word in words:
		insert(root, word)
	# Find and print the longest string with any given prefix in the trie
	print(longest_string_with_all_prefix(root, ""))

# This code is contributed by rambabuguphka
