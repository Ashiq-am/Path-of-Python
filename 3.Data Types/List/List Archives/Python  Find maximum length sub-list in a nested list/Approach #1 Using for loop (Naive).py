# Python3 program to Find maximum
# length list in a nested list

def FindMaxLength(lst):
    maxList = max((x) for x in lst)
    maxLength = max(len(x) for x in lst)

    return maxList, maxLength


# Driver Code
lst = [['A'], ['A', 'B'], ['A', 'B', 'C']]
print(FindMaxLength(lst))
