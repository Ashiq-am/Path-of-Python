# importing string library function
import string


# Function checks if input string
# har only digits or not
def check(value):
    for letter in value:

        # If anything other than digit
        # letter is present, then return
        # False, else return True
        if letter not in string.digits:
            return False
    return True


# Driver Code
input1 = "0123 456 789"
print(input1, "--> ", check(input1))

input2 = "12.0124"
print(input2, "--> ", check(input2))

input3 = "12345"
print(input3, "--> ", check(input3))
