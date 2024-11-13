# Python3 program to Find maximum
# length list in a nested list

def FindMaxLength(lst):
    maxList = max(lst, key=lambda i: len(i))
    maxLength = len(maxList)

    return maxList, maxLength


# Driver Code
lst = [['A'], ['A', 'B'], ['A', 'B', 'C']]
print(FindMaxLength(lst))
