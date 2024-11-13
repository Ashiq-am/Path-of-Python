# Python code to demonstrate working of
# is.lower() method in strings

# Take any string
str = "Live life to the Fullest"

# Traversing Each character of
# the string to check whether
# it is in lowercase
for char in str:
    k = char.islower()
    if k == True:
        print('True')

        # Break the Loop when you
        # get any lowercase character.
        break

# Default condition if the string
# does not have any lowercase character.
if (k != 1):
    print('False')
