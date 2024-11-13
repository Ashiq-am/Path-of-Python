# Python3 program to demonstrate
# error of int() function


# when the binary number is not
# stored in as string
binaryString = 111

# it returns an error for passing an
# integer in place of string
decimal = int(binaryString, 2)

print(decimal)
