# Python3 program for the above approach

# Function to remove sub-directories
# from the given lists dir
def eraseSubdirectory(dir):
    # Store final result
    res = []

    # Sort the given directories
    dir.sort()

    # Insert 1st directory
    res.append(dir[0])

    print("{", dir[0], end=", ")

    # Iterating in directory
    for i in range(1, len(dir)):

        # Current directory
        curr = dir[i]

        # Our previous valid directory
        prev = res[len(res) - 1]

        # Find length of previous directory
        l = len(prev)

        # If subdirectory is found
        if (len(curr) > l and
                curr[l] == '/' and
                prev == curr[:l]):
            continue

        # Else store it in result
        # valid directory
        res.append(curr)
        print(curr, end=", ")

    print("}")


# Driver Code
if __name__ == '__main__':
    # Given lists of directories dir[]
    dir = ["/a", "/a/j", "/c/d/e", "/c/d", "/b"]

    # Function Call
    eraseSubdirectory(dir)

# This code is contributed by akhilsaini
