# Function which returns all strings
# that contains given prefix
from pytrie import StringTrie


def prefixSearch(arr, prefix):
    # create empty trie
    trie = StringTrie()

    # traverse through list of strings
    # to insert it in trie. Here value of
    # key is itself key because at last
    # we need to return
    for key in arr:
        trie[key] = key

    # values(search) method returns list
    # of values of keys which contains
    # search pattern as prefix
    return trie.values(prefix)


# Driver program
if __name__ == "__main__":
    arr = ['geeksforgeeks', 'forgeeks', 'geeks', 'eeksfor']
    prefix = 'geek'
    output = prefixSearch(arr, prefix)
    if len(output) > 0:
        print(output)
    else:
        print('Pattern not found')
