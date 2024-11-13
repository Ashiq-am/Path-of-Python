# Python3 program to find Longest Sum of consecutive
# primes
MAX = 10000;


# utility function for sieve of sundaram
def sieveSundaram(primes):
    # In general Sieve of Sundaram, produces primes smaller
    # than (2*x + 2) for a number given number x. Since
    # we want primes smaller than MAX, we reduce MAX to half
    # This array is used to separate numbers of the form
    # i+j+2ij from others where 1 <= i <= j
    marked = [0 for _ in range(1 + MAX // 2)]

    # Main logic of Sundaram. Mark all numbers which
    # do not generate prime number by doing 2*i+1
    for i in range(1, 1 + (int(MAX ** 0.5) - 1) // 2):
        for j in range((i * (i + 1)) << 1, 1 + MAX // 2, 2 * i + 1):
            marked[j] = True

    # Since 2 is a prime number
    primes.append(2);

    # Print other primes. Remaining primes are of the
    # form 2*i + 1 such that marked[i] is false.
    for i in range(1, 1 + MAX // 2):
        if (marked[i] == False):
            primes.append(2 * i + 1);

    return primes


# function find the prime number which can be written
# as the sum of the most consecutive primes
def LSCPUtil(limit, prime, sum_prime):
    # To store maximum length of consecutive primes that can
    # sum to a limit
    max_length = -1;

    # The prime number (or result) that can be represented as
    # sum of maximum number of primes.
    prime_number = -1;

    # Consider all lengths of consecutive primes below limit.
    i = 0
    while (prime[i] <= limit):
        for j in range(i):

            # if we cross the limit, then break the loop
            if (sum_prime[i] - sum_prime[j] > limit):
                break;

            # sum_prime[i]-sum_prime[j] is prime number or not
            consSum = sum_prime[i] - sum_prime[j];

            # Check if sum of current length of consecutives is
            # prime or not.
            if consSum in prime:
                # update the length and prime number
                if (max_length < i - j + 1):
                    max_length = i - j + 1;
                    prime_number = consSum
        i += 1

    return prime_number;


# Returns the prime number that can written as sum
# of longest chain of consecutive primes.
def LSCP(arr, n):
    # Store prime number in vector
    primes = [];
    primes = sieveSundaram(primes);

    sum_prime = [None for _ in range(1 + len(primes))]

    # Calculate sum of prime numbers and store them
    # in sum_prime array. sum_prime[i] stores sum of
    # prime numbers from primes[0] to primes[i-1]
    sum_prime[0] = 0;
    for i in range(1, 1 + len(primes)):
        sum_prime[i] = primes[i - 1] + sum_prime[i - 1];

    # Process all queries one by one
    for i in range(n):
        print(LSCPUtil(arr[i], primes, sum_prime), end=" ");


# Driver program
arr = [10, 30, 40, 50, 1000];
n = len(arr)
LSCP(arr, n);

# This code is contributed by phasing17
