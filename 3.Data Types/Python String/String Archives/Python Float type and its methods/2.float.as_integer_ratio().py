# Python3 program to illustrate
# working of float.as_integer_ratio()

def frac(d):
    # Using as_integer_ratio
    b = d.as_integer_ratio()

    return b


# Driver code
if __name__ == '__main__':
    b = frac(3.5)
    print(b[0], "/", b[1])
