# Python 3 Program to show working
# of translate() method

# First String
firstString = "gef"

# Second String
secondString = "eks"

# Third String
thirdString = "ge"

# Original String
string = "geeks"
print("Original string:", string)

translation = string.maketrans(firstString, secondString, thirdString)

# Translated String
print("Translated string:",string.translate(translation))
