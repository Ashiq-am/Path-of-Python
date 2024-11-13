# Python3 program for the above approach

# Function to count the number of
# crazy primes in the given range [L, R]
def count_crazy_primes(L, R):
    # Stores all primes
    prime = [0] * (R + 1)

    # Stores count of primes
    countPrime = [0] * (R + 1)

    # Stores if frequency of
    # primes is a prime or not
    # upto each index
    freqPrime = [0] * (R + 1)

    prime[0] = prime[1] = 1

    # Sieve of Eratosthenes
    p = 2
    while p * p <= R:
        if (prime[p] == 0):
            for i in range(p * p,
                           R + 1, p):
                prime[i] = 1
        p += 1

    # Count primes
    for i in range(1, R + 1):
        countPrime[i] = countPrime[i - 1]

        # If i is a prime
        if (not prime[i]):
            countPrime[i] += 1

    # Stores frequency of primes
    for i in range(1, R + 1):
        freqPrime[i] = freqPrime[i - 1]

        # If the frequency of primes
        # is a prime
        if (not prime[countPrime[i]]):
            # Increase count of
            # required numbers
            freqPrime[i] += 1

    # Return the required count
    return (freqPrime[R] -
            freqPrime[L - 1])


# Driver Code
if __name__ == "__main__":
    # Given Range
    L = 4
    R = 12

    # Function Call
    print(count_crazy_primes(L, R))

# This code is contributed by Chitranayal
