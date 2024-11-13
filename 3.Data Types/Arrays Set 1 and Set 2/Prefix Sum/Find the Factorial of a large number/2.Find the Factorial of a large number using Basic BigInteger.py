# Python3 program to find large
# factorials

# Returns Factorial of N
def factorial(N):
    # Initialize result
    f = 1

    # Multiply f with 2, 3, ...N
    for i in range(2, N + 1):
        f *= i

    return f;


# Driver method
N = 20;
print(factorial(N));

# This code is contributed by phasing17
