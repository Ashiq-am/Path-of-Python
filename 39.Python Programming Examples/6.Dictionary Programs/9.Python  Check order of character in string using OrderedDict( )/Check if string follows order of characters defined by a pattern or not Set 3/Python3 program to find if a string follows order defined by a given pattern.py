# Python3 program to find if a string follows
# order defined by a given pattern
CHAR_SIZE = 256


# Returns true if characters of str follow
# order defined by a given ptr.
def checkPattern(Str, pat):
    # Initialize all orders as -1
    label = [-1] * CHAR_SIZE

    # Assign an order to pattern characters
    # according to their appearance in pattern
    order = 1

    for i in range(len(pat)):
        # Give the pattern characters order
        label[ord(pat[i])] = order

        # Increment the order
        order += 1

    # Now one by one check if string
    # characters follow above order
    last_order = -1

    for i in range(len(Str)):
        if (label[ord(Str[i])] != -1):

            # If order of this character is less
            # than order of previous, return false
            if (label[ord(Str[i])] < last_order):
                return False

            # Update last_order for next iteration
            last_order = label[ord(Str[i])]

        # return that str followed pat
    return True


# Driver Code
if __name__ == '__main__':
    Str = "engineers rock"
    pattern = "gsr"

    print(checkPattern(Str, pattern))
