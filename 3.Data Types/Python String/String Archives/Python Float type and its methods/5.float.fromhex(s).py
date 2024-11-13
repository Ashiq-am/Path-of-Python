# Python3 program to illustrate
# working of float.fromhex()

def frac(a):
    # using a float.fromhex()
    a = float.fromhex('0x1.1800000000000p+5')

    return a


# Driver code
if __name__ == '__main__':
    b = frac('0x1.1800000000000p+5')
    print(b)
