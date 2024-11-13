# Python3 program to find union of two
# sorted arrays (Handling Duplicates)
def UnionArray(arr1, arr2):
    # Taking max element present in either array
    m = arr1[-1]
    n = arr2[-1]
    ans = 0

    if m > n:
        ans = m
    else:
        ans = n

    # Finding elements from 1st array
    # (non duplicates only). Using
    # another array for storing union
    # elements of both arrays
    # Assuming max element present
    # in array is not more than 10 ^ 7
    newtable = [0] * (ans + 1)

    # First element is always
    # present in final answer
    print(arr1[0], end=" ")

    # Incrementing the First element's count
    # in it's corresponding index in newtable
    newtable[arr1[0]] += 1

    # Starting traversing the first
    # array from 1st index till last
    for i in range(1, len(arr1)):

        # Checking whether current element
        # is not equal to it's previous element
        if arr1[i] != arr1[i - 1]:
            print(arr1[i], end=" ")
            newtable[arr1[i]] += 1

    # Finding only non common
    # elements from 2nd array
    for j in range(0, len(arr2)):

        # By checking whether it's already
        # present in newtable or not
        if newtable[arr2[j]] == 0:
            print(arr2[j], end=" ")
            newtable[arr2[j]] += 1


# Driver Code
if __name__ == "__main__":
    arr1 = [1, 2, 2, 2, 3]
    arr2 = [2, 3, 4, 5]

    UnionArray(arr1, arr2)
