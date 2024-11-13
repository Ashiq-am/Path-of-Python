# Program to calculate factorial of a number
# using a Tail-Recursive function.

# A tail recursive function
def Recur_facto(n, a=1):
    if (n == 0):
        return a

    return Recur_facto(n - 1, n * a)


# print the result
print(Recur_facto(6))
