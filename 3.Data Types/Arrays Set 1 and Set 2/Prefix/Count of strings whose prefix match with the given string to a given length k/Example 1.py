# Python3 implementation of the approach

# Trie node (considering only lowercase alphabets)
class Node:
    def __init__(self):
        self.arr = [None] * 26
        self.freq = 0


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return Node()

    # Function to insert a node in the trie
    def insert(self, s):

        _in = 0
        cur = self.root
        for i in range(len(s)):
            _in = ord(s[i]) - ord('a')

            # If there is no node created then create one
            if not cur.arr[_in]:
                cur.arr[_in] = self.getNode()

            # Increase the frequency of the node
            cur.arr[_in].freq += 1

            # Move to the next node
            cur = cur.arr[_in]

    # Function to return the count of strings
    # whose prefix of length k matches with the
    # k length prefix of the given string
    def find(self, s, k):

        _in = 0
        count = 0
        cur = self.root

        # Traverse the string
        for i in range(len(s)):
            _in = ord(s[i]) - ord('a')

            # If there is no node then return 0
            if cur.arr[_in] == None:
                return 0

            # Else traverse to the required node
            cur = cur.arr[_in]

            count += 1

            # Return the required count
            if count == k:
                return cur.freq
        return 0


# Driver code
def main():
    arr = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]
    n = len(arr)

    root = Trie();

    # Insert the strings in the trie
    for i in range(n):
        root.insert(arr[i])

    # Query 1
    print(root.find("abbg", 3))

    # Query 2
    print(root.find("abg", 2))

    # Query 3
    print(root.find("xyz", 2))


if __name__ == '__main__':
    main()

# This code is contributed by divyamohan123

