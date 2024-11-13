# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()


print(shout('Hello'))

# Assigning function to a variable
yell = shout

print(yell('Hello'))
