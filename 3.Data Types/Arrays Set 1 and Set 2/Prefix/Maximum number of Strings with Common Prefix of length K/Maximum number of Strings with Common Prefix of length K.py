# Python3 code to implement the approach

# Structure of a Trie Node
class Node:

    # Stores index
    # of string
    def __init__(self):
        self.child = [None] * 26
        self.count = 0


result = 0
K = 0
root = None


# Insert given string into Trie
def insert(s):
    global root
    global result
    global K

    # Initialize a Trie Node curr which
    # point to root initially

    curr = root

    # Iterate over the length of
    # given string
    for i in range(len(s)):

        # Check if Node for current
        # character exit in Trie If not
        # exist then create new Trie node
        # and assign the reference to
        # current node child
        if (not curr.child[ord(s[i]) - ord('a')]):
            # Create a new node of Trie.
            curr.child[ord(s[i]) - ord('a')] = Node()

        # Increment the count of prefix.
        curr.child[ord(s[i]) - ord('a')].count += 1

        # Check if length of the current
        # string becomes greater than
        # required k If true, then maximise
        # longest prefix will result
        if (i + 1 == K):
            result = max(result, curr.child[ord(s[i]) - ord('a')].count)
            break

        # Move the current pointer
        # to next node
        curr = curr.child[ord(s[i]) - ord('a')]

    return curr


# Driver Code
if __name__ == '__main__':
    arr = ["hello", "heydeei", "hap", "hak", "paloa", "padfk", "padfla", "pada"]
    K = 4

    N = len(arr)
    root = Node()

    for i in range(N):
        insert(arr[i])

    print(result)

# This code is contributed by Aman Kumar
