# Python 3 implementation for representing
# each word in a sentence as sum of
# ASCII values of each word

# Function to compute the sum of ASCII
# values of each word separated by a space
# and return the total sum of the ASCII
# values, excluding the space.
def ASCIIWordSum(str, sumArr):
    l = len(str)
    sum = 0
    bigSum = 0
    for i in range(l):

        # Separate each word by a space
        # and store values corresponding
        # to each word
        if (str[i] == ' '):

            bigSum += sum
            sumArr.append(sum)
            sum = 0

        else:

            # Implicit type casting
            sum += ord(str[i])

        # Storing the value of last word
    sumArr.append(sum)
    bigSum += sum
    return bigSum


# Driver Code
if __name__ == "__main__":

    str = "GeeksforGeeks a computer science portal for Geeks"
    sumArr = []

    # Calling function
    sum = ASCIIWordSum(str, sumArr)

    print("Sum of ASCII values:")
    for x in sumArr:
        print(x, end=" ")

    print()
    print("Total sum -> ", sum)
