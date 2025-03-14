# import the math module
import math


# function
def Elias_Gamma_Decoding(x):
    x = list(x)
    K = 0
    while True:
        if not x[K] == '0':
            break
        K = K + 1

    # Reading K more bits from '1'
    x = x[K:2 * K + 1]

    n = 0
    x.reverse()

    # Converting binary to integer
    for i in range(len(x)):
        if x[i] == '1':
            n = n + math.pow(2, i)
    return int(n)


# value input
x = '0001001'

# call the function
print(Elias_Gamma_Decoding(x))
