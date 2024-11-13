# Python3 program to print the pattern
# hollow square with plus inside it
# window pattern


# function to print pattern n means
# number of rows which we want
def window_pattern(n):
    # if n is odd then we will have
    # only one middle element
    if n % 2 != 0:
        c = (n // 2) + 1
        d = 0

    # if n is even then we will have two
    # values
    else:
        c = (n // 2) + 1
        d = (n // 2)

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            # if i,j equals to corner row or
            # column then "*"
            if i == 1 or j == 1 or i == n or j == n:
                print("*", end=" ")

            else:

                # if i,j equals to the middle row
                # or column then "*"
                if i == c or j == c:
                    print("*", end=" ")

                elif i == d or j == d:
                    print("*", end=" ")

                else:
                    print(" ", end=" ")

        print()


# Driver Code
if __name__ == "__main__":
    n = 7
    window_pattern(n)
