# Python implementation of above program

# Function to check if a
# string is a palindrome or not
def palindrome(string):
    if (string == string[::-1]):
        return True
    else:
        return False


# Function to print the updated sentence
def printSortedPalindromes(sentence):
    # Stores palindromic words
    newlist = []

    # Stores the words split by spaces
    lis = list(sentence.split())

    # Traversing the list
    for i in lis:

        # If current word is palindrome
        if (palindrome(i)):
            # Update newlist
            newlist.append(i)

    # Sort the words in newlist
    newlist.sort()

    # Pointer to iterate newlis
    j = 0

    # Traverse the list
    for i in range(len(lis)):

        # If current word is palindrome
        if (palindrome(lis[i])):
            # Replacing word with
            # current word in newlist
            lis[i] = newlist[j]

            # Increment j by 1
            j = j + 1

    # Print the updated sentence
    for i in lis:
        print(i, end=" ")


# Driver Code

sentence = "please refer to the madam to know the level"

printSortedPalindromes(sentence)
