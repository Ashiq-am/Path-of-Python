# importing string library function
import string


# Function checks if input string
# has upper ascii letters or not
def check(value):
    for letter in value:

        # If anything other than upper ascii
        # letter is present, then return
        # False, else return True
        if letter not in string.ascii_uppercase:
            return False
    return True


# Driver Code
input1 = "GeeksForGeeks"
print(input1, "--> ", check(input1))

input2 = "GEEKS FOR GEEKS"
print(input2, "--> ", check(input2))

input3 = "GEEKSFORGEEKS"
print(input3, "--> ", check(input3))
