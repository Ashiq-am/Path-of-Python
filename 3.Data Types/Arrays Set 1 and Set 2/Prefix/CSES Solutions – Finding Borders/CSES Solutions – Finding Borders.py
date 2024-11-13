# Importing the required libraries
import math

# Constants
MOD = int(1e9) + 7
p1 = 31
p2 = 37
maxN = int(1e6) + 5

# Variables
pow1 = [0]*maxN
pow2 = [0]*maxN
ph1 = ph2 = sh1 = sh2 = 0

# Function to find borders
def solve(S, N):
    global pow1, pow2, ph1, ph2, sh1, sh2

    # Initialize the powers of p1 and p2
    pow1[0] = pow2[0] = 1
    for i in range(1, N):
        pow1[i] = (pow1[i - 1] * p1) % MOD
        pow2[i] = (pow2[i - 1] * p2) % MOD

    # Calculate the prefix and suffix hashes
    for i in range(N - 1):
        l = ord(S[i]) - ord('a') + 1
        r = ord(S[N - i - 1]) - ord('a') + 1

        ph1 = (ph1 + l * pow1[i]) % MOD
        ph2 = (ph2 + l * pow2[i]) % MOD
        sh1 = (sh1 * p1 + r) % MOD
        sh2 = (sh2 * p2 + r) % MOD

        # If the prefix and suffix hashes are equal, print
        # the length of the border
        if ph1 == sh1 and ph2 == sh2:
            print(i + 1, end=" ")

# Driver code
if __name__ == "__main__":
    # Read the input string
    S = "abcababcab"
    N = len(S)
    solve(S, N)
