def miller_rabin(n, k):
    """
    Performs the Miller-Rabin primality test on a number n with k iterations.
    """

    # 1. Handle special cases: 0, 1, 4 are not prime.
    if n <= 1 or n == 4:
        return False

    # 2. Find d and s such that n - 1 = 2^s * d (where d is odd).
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # 3. Perform k iterations of the test.
    for _ in range(k):
        # 4. Choose a random integer a between 2 and n-2.
        a = random.randint(2, n - 2)

        # 5. Calculate x = a^d mod n.
        x = pow(a, d, n)

        # 6. Check if x is 1 or n-1:
        #   - If x is 1, the test is inconclusive.
        #   - If x is n-1, the test is inconclusive.
        if x == 1 or x == n - 1:
            continue

        # 7. Repeat steps 5 and 6 for s-1 times.
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break

        # 8. If x is not n-1 after s-1 iterations, n is composite.
        if x != n - 1:
            return False

    # 9. If all iterations pass, n is probably prime.
    return True
