# Python program to check if there
# is k consecutive 1's in a binary number

# function to check if there are k
# consecutive 1's
def check(s, k):
    # form a new string of k 1's
    new = "1" * k

    # if there is k 1's at any position
    if new in s:
        print("yes")
    else:
        print("no")


# driver code
s = "10101001111"
k = 4
check(s, k)
