# Python implementation to replace nth
# occurrence of the every character
# in a string

# Function to replace the Nth occurence
# of the character of string
def replacer(initial_string, ch,
             replacing_character, occurrence):
    # breaking a string into it's
    # every single character in list
    lst1 = list(initial_string)
    lst2 = list(ch)

    # List to store the indexes in which
    # it is replaced with the
    # replacing_character
    lst3 = []

    # Loop to find the Nth occurence of
    # given characters in the string
    for i in lst2:
        if (lst1.count(i) >= occurrence):
            count = 0
            for j in range(0, len(initial_string)):
                if (i == lst1[j]):
                    count += 1
                    if (count == occurrence):
                        lst3.append(j)

    for i in lst3:
        # Replacing that particular index
        # with the requested character
        lst1[i] = replacing_character

    print(''.join(lst1))


# Driver Code:
if __name__ == '__main__':
    initial_string = 'GeeksforGeeks'
    ch = ['G', 'e', 'k']
    occurence = 2
    replacing_character = '#'
    replacer(initial_string, ch,
             replacing_character, occurence)
