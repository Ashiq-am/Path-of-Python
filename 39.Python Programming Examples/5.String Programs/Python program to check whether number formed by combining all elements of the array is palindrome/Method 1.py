# function to check palindrome
def checkPalindrome(string):
    # reverse the string
    rev = string[::-1]

    # checking if string is equal to reverse
    if (string == rev):
        return True
    else:
        return False


# function to convert list to single number string
def joinArray(lis):
    # convert the elements of list to string
    lis = list(map(str, lis))

    # converting list to string
    number = ''.join(lis)

    # checking if it is palindrome
    if (checkPalindrome(number)):
        return True
    else:
        return False


# Driver code
lis = [1, 76, 39, 93, 67, 1]
if (joinArray(lis)):
    print("Palindrome")
else:
    print("not Palindrome")
