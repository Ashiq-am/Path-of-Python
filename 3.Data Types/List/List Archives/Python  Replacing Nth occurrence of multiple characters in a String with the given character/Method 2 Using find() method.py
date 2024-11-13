# Python implementation to replace nth
# occurrence of the every character
# in a string using find() function

# Function to replace the Nth occurence
# of the character of string
def replacer(initial_string, ch,
             replacing_character, occurrence):
    # breaking a string into
    # it's every single character
    lst1 = list(initial_string)
    lst2 = list(ch)

    # Loop to find the occurrence
    # of the character in the string
    # and replace it with the given
    # replacing_character
    for i in lst2:
        sub_string = i
        val = -1
        for i in range(0, occurrence):
            val = initial_string.find(sub_string,
                                      val + 1)
        lst1[val] = replacing_character

    print(''.join(lst1))


# Driver Code:
if __name__ == '__main__':
    initial_string = 'GeeksforGeeks'
    ch = ['G', 'e', 'k']
    occurence = 2
    replacing_character = '#'
    replacer(initial_string, ch,
             replacing_character, occurence)
