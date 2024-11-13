# Python code for the above approach

# Function to solve the problem
def minRemoval(s):
    # Storing prefixSum with index of
    # its first occurance.
    mp = {}
    n = len(s)

    # For storing the prefix Sum ending
    # at ith index
    prefixSum = 0

    # For keeping the length of longest
    # binary string where number of zero
    # and ones are equal.
    result = 0

    # Iterate over the string
    for i in range(n):
        prefixSum += 1 if (s[i] == '1') else -1

        if prefixSum is 0:
            result = max(result, i + 1)

        # Check if prefixSum have previously
        # occured or not
        if prefixSum in mp:

            # Update the result with this
            # valid substring
            result = max(result, i - mp[prefixSum])
        else:
            # Store this prefixSum has occur at
            # ith index in the map.
            mp[prefixSum] = i

    # Return the remaining length other
    # than the longest valid substring.
    return n - result


S = "0111010"

# Function call
result = minRemoval(S)
print(result)

# This code is contributed by lokesh.
