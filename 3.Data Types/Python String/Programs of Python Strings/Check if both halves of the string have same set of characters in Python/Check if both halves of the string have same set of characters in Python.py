# Function to Check if both halves of
# the string have same set of characters
from collections import Counter


def checkTwoHalves(input):
    length = len(input)

    # Break input string in two parts
    if (length % 2 != 0):
        first = input[0:length // 2]
        second = input[(length // 2) + 1:]
    else:
        first = input[0:length // 2]
        second = input[length // 2:]

    # Convert both halves into dictionary and compare
    if Counter(first) == Counter(second):
        print('YES')
    else:
        print('NO')

    # Driver program


if __name__ == "__main__":
    input = 'abbaab'
    checkTwoHalves(input)
