# Python3 Program to find depth of a dictionary
def dict_depth(myDict):
    Ddepth = 1
    obj = [(k, Ddepth + 1) for k in myDict.values()
           if isinstance(k, dict)]
    max_depth = 0

    while (obj):
        n, Ddepth = obj.pop()
        max_depth = max(max_depth, Ddepth)

        obj = obj + [(k, Ddepth + 1) for k in n.values()
                     if isinstance(k, dict)]

    return max_depth


# Driver code
myDict = {1: 'a', 2: {3: {4: {}}}}
print(dict_depth(myDict))
