# Python3 implementation to remove all the
# palindromic words from the given sentence

# function to check if 'str' is palindrome
def isPalindrome(string):
    i = 0
    j = len(string) - 1

    # traversing from both the ends
    while (i < j):

        # not palindrome
        if (string[i] != string[j]):
            return False
        i += 1
        j -= 1

    # palindrome
    return True


# function to remove all the palindromic words
# from the given sentence
def removePalinWords(string):
    # 'final_str' to store the final string and
    # 'word' to one by one store each word of 'str'
    final_str = ""
    word = ""

    # add space at the end of 'str'
    string = string + " "
    n = len(string)

    # traversing 'str'
    for i in range(n):

        # accumulating characters of the current word
        if (string[i] != ' '):
            word = word + string[i]

        else:

            # if 'word' is not palindrome then a
            # add it to 'final_str'
            if (not (isPalindrome(word))):
                final_str += word + " "

            # reset
            word = ""

    # required final string
    return final_str


# Driver Code
if __name__ == "__main__":
    string = "Text contains malayalam and level words"
    print(removePalinWords(string))

