# Python3 program to Convert a list
# of lists into Dictionary (Tree form)

def formTree(list):
    tree = {}
    for item in list:
        currTree = tree

        for key in item[::-1]:
            if key not in currTree:
                currTree[key] = {}
            currTree = currTree[key]

    return tree


# Driver Code
lst = [['A'], ['B', 'A'], ['C', 'A'], ['D', 'C', 'A']]
print(formTree(lst))
