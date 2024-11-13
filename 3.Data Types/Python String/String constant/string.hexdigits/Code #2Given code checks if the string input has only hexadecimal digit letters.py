# importing string library function
import string


# Function checks if input string
# has only hexdigits or not
def check(value):
    for letter in value:

        # If anything other than hexdigit
        # letter is present, then return
        # False, else return True
        if letter not in string.hexdigits:
            return False
    return True


# Driver Code
input1 = "0123456789abcdef"
print(input1, "--> ", check(input1))

input2 = "abcdefABCDEF"
print(input2, "--> ", check(input2))

input3 = "abcdefghGEEK"
print(input3, "--> ", check(input3))
