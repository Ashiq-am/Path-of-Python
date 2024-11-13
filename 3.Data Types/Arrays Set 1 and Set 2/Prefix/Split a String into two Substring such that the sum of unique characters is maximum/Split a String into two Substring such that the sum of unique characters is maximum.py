# Python code for the above approach:
def unique_charcters(str, n):
    # Declare set to check if the current
    # character is previously
    # appearing or not
    s1 = set()
    s2 = set()

    # Store the count of unique characters
    # from starting index.
    prefix = [0]*n

    # Store the count of unique characters
    # from last index.
    suffix = [0]*n


    prefix[0] = 1
    suffix[n - 1] = 1
    s1.add(str[0])
    s2.add(str[n - 1])

    # Storing the count of unique characters
    # from starting index to last index
    for i in range(1, n):

        # If the current character has
        # appeared before, store
        # previous value
        if str[i] in s1:
            prefix[i] = prefix[i - 1]

        else:
            # else store previous value + 1.
            prefix[i] = prefix[i - 1] + 1
            s1.add(str[i])

    # Storing the count of unique
    # characters from last index
    # to 0th index
    for i in range(n-2, -1, -1):

        # If the current character has
        # already appeared, store the
        # value calculated for the
        # previous visited index of string
        if str[i] in s2:
            suffix[i] = suffix[i + 1]

        else:
            # Else store value on next index + 1.
            suffix[i] = suffix[i + 1] + 1
            s2.add(str[i])

    # Store the maximum sum
    maxi = -1
    for i in range(1, n):
        # Take sum of prefix[i-1] +
        # suffix[i] so that the
        # intersecting never counts.
        maxi = max(maxi, prefix[i - 1] + suffix[i])

    # Returning the maximum value
    return maxi

if __name__ == "__main__":
    str = "abcabcd"

    # Size of the string
    n = len(str)

    # Function call
    print("Maximum sum is ", unique_charcters(str, n))
