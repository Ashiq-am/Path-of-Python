# Python code to implement the above approach

# Final string after performing all the
# operations
def findFinalString(arr, n, ch):
    li = []
    found = 0
    for i in range(n):

        # ch found
        if arr[i] == ch:
            found = 1 - found

        # Push character at front of list
        if found:
            li.insert(0, arr[i])
        # Push character at back of list
        else:
            li.append(arr[i])

    # If there is odd number of ch
    if found == 1:
        li = li[::-1]

    # Return the list
    return li


# Driver Code
if __name__ == "__main__":
    arr = ['A', 'B', 'X', 'C', 'D', 'X', 'F']
    ch = 'X'
    N = len(arr)

    # Function call
    ans = findFinalString(arr, N, ch)
    for val in ans:
        print(val, end=" ")

# This Code is Contributed By Vivek Maddeshiya
