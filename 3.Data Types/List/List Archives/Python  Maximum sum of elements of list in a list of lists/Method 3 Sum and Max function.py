# Python program to find the
# list in a list of lists whose
# sum of elements is the highest
# using sum and max function

def maximumSum(list1):
    return (sum(max(list1, key=sum)))


# driver code
list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximumSum(list1))
