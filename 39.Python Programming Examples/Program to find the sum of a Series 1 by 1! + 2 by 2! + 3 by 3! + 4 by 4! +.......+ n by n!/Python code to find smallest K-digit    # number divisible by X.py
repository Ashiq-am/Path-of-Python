# Python code to find smallest K-digit
# number divisible by X

def sumOfSeries(num):
    # Computing MAX
    res = 0
    fact = 1

    for i in range(1, num + 1):
        fact *= i
        res = res + (i / fact)

    return res


n = 5
print("Sum: ", sumOfSeries(n))
