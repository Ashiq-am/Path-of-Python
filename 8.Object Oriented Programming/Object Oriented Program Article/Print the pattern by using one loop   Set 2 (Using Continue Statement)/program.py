# Python 3 program to print
# a pattern using single
# loop and continue statement

# printPattern function
# to print pattern
def printPattern(n):
    # Variable initialization
    line_no = 1  # Line count

    # Loop to print
    # desired pattern
    curr_star = 0
    line_no = 1
    while (line_no <= n):

        # If current star count
        # is less than current
        # line number
        if (curr_star < line_no):
            print("* ", end="")
            curr_star += 1
            continue

        # Else time to print
        # a new line
        if (curr_star == line_no):
            print("")
            line_no += 1
            curr_star = 0


# Driver code
printPattern(7)


