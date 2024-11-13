# Recursive function to print the Fibonacci series
def fib(n, prev1, prev2):
    if n < 3:
        return
    fn = prev1 + prev2
    prev2 = prev1
    prev1 = fn
    print(fn, end=" ")
    fib(n - 1, prev1, prev2)

def print_fib(n):
    # When the number of terms is less than 1
    if n < 1:
        print("Invalid number of terms")
    elif n == 1:
        print(0)
    elif n == 2:
        print("0 1")
    else:
        print("0 1", end=" ")
        fib(n, 1, 0)

# Driver code
if __name__ == "__main__":
    n = 9
    # Function call
    print_fib(n)
