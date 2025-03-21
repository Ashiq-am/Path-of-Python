# Python3 program to answer queries for
# count of primes in given range.
MAX = 10000

# prefix[i] is going to
# store count of primes
# till i (including i).
prefix = [0] * (MAX + 1)


def buildPrefix():
    # Create a boolean array value in
    # prime[i] will "prime[0..n]". A
    # finally be false if i is Not a
    # prime, else true.
    prime = [1] * (MAX + 1)

    p = 2
    while (p * p <= MAX):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == 1):

            # Update all multiples of p
            i = p * 2
            while (i <= MAX):
                prime[i] = 0
                i += p
        p += 1

    # Build prefix array
    # prefix[0] = prefix[1] = 0;
    for p in range(2, MAX + 1):
        prefix[p] = prefix[p - 1]
        if (prime[p] == 1):
            prefix[p] += 1


# Returns count of primes
# in range from L to
# R (both inclusive).
def query(L, R):
    return prefix[R] - prefix[L - 1]


# Driver code
if __name__ == '__main__':
    buildPrefix()

    L = 5
    R = 10
    print(query(L, R))

    L = 1
    R = 10
    print(query(L, R))
