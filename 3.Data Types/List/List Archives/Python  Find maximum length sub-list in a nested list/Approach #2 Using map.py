# Python3 program to Find maximum
# length list in a nested list

def FindMaxLength(lst):
    maxList = max(lst, key=len)
    maxLength = max(map(len, lst))

    return maxList, maxLength


# Driver Code
lst = [['A'], ['A', 'B'], ['A', 'B', 'C'], ]
print(FindMaxLength(lst))
