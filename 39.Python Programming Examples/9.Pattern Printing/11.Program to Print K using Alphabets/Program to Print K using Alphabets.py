# Python Program to design the
# above pattern of K using alphabets

# Function to print the above Pattern
def display(n):
    v = n

    # This loop is used for rows and
    # prints the alphabets in decreasing
    # order
    while (v >= 0):
        c = 65

        # This loop is used for columns
        for j in range(v + 1):
            # chr() function converts the
            # number to alphabet
            print(chr(c + j), end=" ")
        v = v - 1
        print()

    # This loop is again used to rows and
    # prints the half remaining pattern in
    # increasing order
    for i in range(n + 1):
        c = 65

        for j in range(i + 1):
            print(chr(c + j), end=" ")
        print()


# Driver code
n = 3
display(n)
