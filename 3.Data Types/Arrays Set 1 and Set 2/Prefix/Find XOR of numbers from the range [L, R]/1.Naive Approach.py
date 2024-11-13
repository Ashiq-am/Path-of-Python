# Python3 implementation of the approach
from operator import xor

# Function to return the XOR of elements
# from the range [1, n]
def findXOR(l, r):

    ans = 0
    for i in range(l,r+1):
        ans = xor(ans,i)
    return ans

# Driver code
l = 4; r = 8

print(findXOR(l, r))

# This code is contributed by Arpit Jain
