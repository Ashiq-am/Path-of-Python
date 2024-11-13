# Python program for the above approach

# Function which returns last word
def removePalindrome(string):
    # Split by space and converting
    # String to list and
    lis = list(string.split(" "))

    # length of list
    length = len(lis)

    # Taking new list
    newlis = []

    # loop till length of list
    for i in range(length):

        # check if the word is palindrome
        if (lis[i] != lis[i][::-1]):
            newlis.append(lis[i])

    return newlis


# Driver code
string = "Text contains malayalam and level words"
print(*removePalindrome(string))
