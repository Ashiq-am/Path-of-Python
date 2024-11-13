# Python implementation to replace nth
# occurrence of the every character
# in a string

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
    for j in lst2:
        sub_string = j
        checklist = [i for i in range(0, len(initial_string))
                     if initial_string[i:].startswith(sub_string)]
        if len(checklist) >= occurrence:
            lst1[checklist[occurrence - 1]] = replacing_character

    print(''.join(lst1))


# Driver Code:
if __name__ == '__main__':
    initial_string = 'GeeksforGeeks'
    ch = ['G', 'e', 'k']
    occurence = 2
    replacing_character = '#'
    replacer(initial_string, ch,
             replacing_character, occurence)
