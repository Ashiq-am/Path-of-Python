# Python 3 program to find largest substring
# having count of 1s more than count
# count of 0s.

# Function to find longest substring
# having count of 1s more than count
# of 0s.
def findLongestSub(bin1):
    n = len(bin1)

    # To store sum.
    sum = 0

    # To store first occurrence of each
    # sum value.
    prevSum = {i: 0 for i in range(n)}

    # To store maximum length.
    maxlen = 0

    # To store current substring length.
    for i in range(n):

        # Add 1 if current character is 1
        # else subtract 1.
        if (bin1[i] == '1'):
            sum += 1
        else:
            sum -= 1

        # If sum is positive, then maximum
        # length substring is bin1[0..i]
        if (sum > 0):
            maxlen = i + 1

        # If sum is negative, then maximum
        # length substring is bin1[j+1..i], where
        # sum of substring bin1[0..j] is sum-1.
        elif (sum <= 0):
            if ((sum - 1) in prevSum):
                currlen = i - prevSum[sum - 1]
                maxlen = max(maxlen, currlen)

            # Make entry for this sum value in hash
        # table if this value is not present.
        if ((sum) not in prevSum):
            prevSum[sum] = i

    return maxlen


# Driver code
if __name__ == '__main__':
    bin1 = "1010"
    print(findLongestSub(bin1))
