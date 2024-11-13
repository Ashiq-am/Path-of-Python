# Python program to Check if a large number can be divided
# into two or more segments of equal sum
# Function to check if a number
# can be divided into segments
def check(s):
    # length of string
    n = len(s)

    # array to store prefix sum
    Presum = [0] * n

    # ord() gives ASCII value
    # first index
    Presum[0] = ord(s[0]) - ord('0')

    # calculate the prefix
    for i in range(n):
        Presum[i] = Presum[i - 1] + (ord(s[i]) - ord('0'))

    # iterate for all number from second number
    for i in range(n):

        # sum from 0th index to i-1th index
        sum = Presum[i]
        presum = 0
        it = 1

        # counter turns true when sum
        # is obtained from a segment
        flag = 0

        # iterate till the last number
        while (it < n):

            # sum of segments
            presum += ord(s[it]) - ord('0')

            # if segment sum is equal
            # to first segment
            if presum == sum:
                presum = 0
                flag = 1

            # when greater than not possible
            elif presum > sum:
                break

            it += 1

        # if at the end all values are traversed
        # and all segments have sum equal to first segment
        # then it is possible
        if presum == 0 and it == n and flag == 1:
            return True

    return False


# Driver Code
if __name__ == "__main__":

    s = "73452"
    if check(s):
        print("Yes")
    else:
        print("No")
