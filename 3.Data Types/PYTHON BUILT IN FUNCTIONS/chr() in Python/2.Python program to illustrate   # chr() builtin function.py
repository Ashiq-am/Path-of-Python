# Python program to illustrate
# chr() builtin function

numbers = [17, 38, 79]

for number in numbers:
    # Convert ASCII-based number to character.
    letter = chr(number)
    print("Character of ASCII value", number, "is ", letter)
