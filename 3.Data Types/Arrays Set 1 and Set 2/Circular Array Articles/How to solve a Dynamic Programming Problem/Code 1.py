# Returns the number of arrangements to
# form 'n'
def solve(n):


    if n < 1:
        return 0

    if n == 1:
        return 1


    return (solve(n - 1) +solve(n - 3) + solve(n - 5))


