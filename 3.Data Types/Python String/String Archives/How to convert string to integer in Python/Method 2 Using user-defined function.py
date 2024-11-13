# User-defined function to
# convert a string into integer
def string_to_int(input_string):


    output_int = 0

    # Check if the number contains
    # any minus sign or not,
    # i.e. is it a negative number or not.
    # If it contains in the first
    # position in a minus sign,
    # we start our conversion
    # from the second position which
    # contains numbers.
    if input_string[0] == '-':
        starting_idx = 1
        check_negative = True


    else:
        starting_idx = 0
        check_negative = False



    for i in range(starting_idx, len(input_string)):
        # calculate the place value for
        # the respective digit
        place_value = 10 ** (len(input_string) - (i + 1))

        # calculate digit value
        # ord() function gives Ascii value
        digit_value = ord(input_string[i]) - ord('0')

        # calculating the final integer value
        output_int += place_value * digit_value

    # if check_negative is true
    # then final integer value
    # is multiplied by -1
    if check_negative:

        return -1 * output_int

    else:
        return output_int

# Driver code
if __name__ == "__main__":
    string = "554"

    # function call
    x = string_to_int(string)

    # Show the Data type
    print(type(x))


    string = "123"

    # Show the Data type


    print(type(string_to_int(string)))


    string = "-123"

    # Show the Data type
    print(type(string_to_int(string)))
