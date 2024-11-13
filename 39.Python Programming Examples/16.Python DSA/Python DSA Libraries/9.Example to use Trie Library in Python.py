from trie import Trie

# Create a new Trie object
trie = Trie()

# Insert some words into the trie
trie.insert("apple")
trie.insert("banana")
trie.insert("app")
trie.insert("bat")
trie.insert("ball")

# Search for words in the trie
print("Search Results:")
print("Does 'apple' exist?", trie.search("apple")) # Output: True
print("Does 'app' exist?", trie.search("app"))	 # Output: True
print("Does 'orange' exist?", trie.search("orange")) # Output: False

# Check if any word starts with a given prefix
print("\nStartsWith Results:")
print("Does any word start with 'ap'?", trie.startswith("ap")) # Output: True
print("Does any word start with 'ora'?", trie.startswith("ora")) # Output: False

# Get autocomplete suggestions for a given prefix
print("\nAutocomplete Suggestions for 'ba':", trie.autocomplete("ba")) # Output: ['ball', 'banana', 'bat']

# Delete a word from the trie
trie.delete("apple")
print("\nAfter deleting 'apple':", trie.words()) # Output: ['app', 'ball', 'banana', 'bat']

# Count the total number of words in the trie
print("\nTotal Number of Words:", trie.count_words()) # Output: 4

# Count the number of words with a given prefix
print("Number of words with prefix 'ba':", trie.count_prefixes("ba")) # Output: 3
