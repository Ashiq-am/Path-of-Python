# Python code to demonstrate working of
# bin()

# function returning binary string
def Binary(n):
    s = bin(n)

    # removing "0b" prefix
    s1 = s[2:]
    return s1


print("The binary representation of 100 (using bin()) is : ", end="")
print(Binary(100))
