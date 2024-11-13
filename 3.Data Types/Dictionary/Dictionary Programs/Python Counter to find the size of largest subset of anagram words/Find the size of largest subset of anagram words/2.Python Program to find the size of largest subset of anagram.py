# Python Program to find the size of
# largest subset of anagram

# Utility function to find size of
# largest subset of anagram
def largestAnagramSet(arr, n):
    maxSize = 0

    # Initialize dictionary of array
    count = {}
    for i in range(n):

        # list to store
        # frequency of element
        freq = [0 for i in range(26)]

        for ch in arr[i]:
            freq[ord(ch) - ord('a')] += 1

        # Increment the count of
        # frequency array in dictionary
        temp = "".join(str(i) for i in freq)
        if temp not in count:
            count[temp] = 1
        else:
            count[temp] += 1

        # Compute the maximum size
        maxSize = max(maxSize, count[temp])
    return maxSize


# Driver code
arr = ["ant", "magenta", "magnate", "tan", "gnamate"]
n = len(arr)
print(largestAnagramSet(arr, n))

arr1 = ["cars", "bikes", "arcs", "steer"]
n = len(arr1)
print(largestAnagramSet(arr1, n))
