def separateNumbersAlphabets(str):
    # Create empty strings for storing the alphabets and numbers
    numbers = ''
    alphabets = ''

    # Iterate through each character in the given string
    for char in str:
        # Check if the character is an alphabet
        if char.isalpha():
            # If it is an alphabet, append it to the alphabets string
            alphabets += char
        # Check if the character is a number
        elif char.isnumeric():
            # If it is a number, append it to the numbers string
            numbers += char

    # Print the final alphabets and numbers strings
    print(numbers)
    print(alphabets)


# Driver code
str = "adbv345hj43hvb42"
separateNumbersAlphabets(str)
