# function to Reverse an array in groups of given size

def reverseGroup(a, k):
    # take an empty list
    res = []

    # iterate over the list with increment of
    # k times in each iteration
    for i in range(0, len(a), k):
        # reverse the list in each iteration over
        # span of k elements using extend
        res.extend((a[i:i + k])[::-1])
        print(res)

# Driver program
if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 5
    reverseGroup(input, k)
