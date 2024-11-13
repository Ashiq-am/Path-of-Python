# importing string library function
import string


# Function checks if input string
# has only octdigits or not
def check(value):
    for letter in value:

        # If anything other than octdigit
        # letter is present, then return
        # False, else return True
        if letter not in string.octdigits:
            return False
    return True


# Driver Code
input1 = "01234567"
print(input1, "--> ", check(input1))

input2 = "abcdefABCDEF"
print(input2, "--> ", check(input2))

input3 = "abcdefghGEEK"
print(input3, "--> ", check(input3))

input4 = "0123"
print(input3, "--> ", check(input4))

input5 = "567"
print(input3, "--> ", check(input5))
