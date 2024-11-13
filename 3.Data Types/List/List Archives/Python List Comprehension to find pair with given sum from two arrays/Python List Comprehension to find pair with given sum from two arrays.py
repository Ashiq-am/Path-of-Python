# Function to find all pairs whose sum is x in
# two arrays

def allPairs(arr1, arr2, x):
    # finds all pairs in two arrays
    # whose sum is x
    print([(x - k, k) for k in arr2 if (x - k) in arr1])


# Driver program
if __name__ == "__main__":
    arr1 = [-1, -2, 4, -6, 5, 7]
    arr2 = [6, 3, 4, 0]
    x = 8
    allPairs(arr1, arr2, x)
