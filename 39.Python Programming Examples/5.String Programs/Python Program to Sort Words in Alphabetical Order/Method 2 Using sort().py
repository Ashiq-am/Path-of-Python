# Python3 program to sort the words of a
# string in alphabetical order
# Function to sort the words in alphabetical
# order
def F(S):
    W = S.split("")

    for i in range(len(W)):
        W[i] = W[i].lower()
        W.sort()

    # return the sorted words
    return "".join(W)

# Driver code
S = "GeekS for geEks"
print(F(S))