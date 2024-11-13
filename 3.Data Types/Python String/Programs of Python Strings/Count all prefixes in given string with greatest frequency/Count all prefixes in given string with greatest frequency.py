# Python program to Count all
# prefixes in given string with
# greatest frequency

# Function to print the prefixes
def prefix(string1, alphabet1, alphabet2):
    count = 0
    non_empty_string = ""

    string2 = list(string1)

    # Loop for iterating the length of
    # the string and print the prefixes
    # and the count of query prefixes.
    for i in range(0, len(string2)):
        non_empty_string = non_empty_string + (string2[i])

        if (non_empty_string.count(alphabet1) >
                non_empty_string.count(alphabet2)):
            # prints all required prefixes
            print(non_empty_string)

            # increment count
            count += 1

    # returns count of the
    # required prefixes
    return (count)


# Driver Code
print(prefix("geeksforgeeks", "e", "g"))
