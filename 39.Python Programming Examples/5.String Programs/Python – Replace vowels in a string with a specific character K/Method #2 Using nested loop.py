# Function to Replace each vowel
# in the string with a specified character
def replaceVowelsWithK(test_str, K):
    # creating list of vowels
    vowels_list = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    # creating empty list
    new_string = []

    # converting the given string to list
    string_list = list(test_str)

    # running 1st iteration for
    # comparing all the
    # characters of string with
    # the vowel characters
    for char in string_list:

        # running 2nd iteration for
        # comparing all the characters
        # of vowels with the string character
        for char2 in vowels_list:

            # comparing string character
            # and vowel character
            if char == char2:
                # if condition is true then adding
                # the specific character entered
                # by the user in the new list
                new_string.append(K)
                break

        # else adding the character
        else:
            new_string.append(char)

        # return the converted list into string
    return (''.join(new_string))


# Driver Code
# input string
input_str = "Geeks for Geeks"

# specified character
K = "#"

# printing input
print("Given Sting:", input_str)
print("Given Specified Character:", K)

# printing output
print("Afer replacing vowels with the specified character:",
      replaceVowelsWithK(input_str, K))
