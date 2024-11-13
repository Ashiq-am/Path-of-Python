# function to find the length of the
# merged string

def mergedstring(x, y):
    k = len(y)
    for i in range(len(x)):

        if x[i:] == y[:k]:
            break
        else:
            k = k - 1

    # uncomment the below statement to
    # know what the merged string is
    # print(a + b[k:])
    return len(a + b[k:])


# function to find the minimum length
# among the merged string
def merger(a, b):
    # reverse b
    b1 = b[::-1]

    # function call to find the length
    # of string without reversing string 'B'
    r1 = mergedstring(a, b)

    # function call to find the length
    # of the string by reversing string 'B'
    r2 = mergedstring(a, b1)

    # compare between lengths
    if r1 > r2:
        print("Length is", r2)
    else:
        print("Length is", r1)

    # driver code


a = "abcbc"
b = "bcabc"

merger(a, b)
