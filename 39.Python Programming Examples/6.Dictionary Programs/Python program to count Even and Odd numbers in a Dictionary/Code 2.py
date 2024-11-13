# Python3 Program to count even
# and odd elements in a dictionary

# Function to count even and
# odd elements in a dictionary
def countEvenOdd(dict):
    even = 0


odd = 0

# Iterate over the dictionary
for i in dict:

    # If current element is even
    if dict[i] % 2 == 0:

        # Increase count of even
        even = even + 1

    # Otherwise
    else:

        # Increase count of odd
        odd = odd + 1

print("Even count: ", even)
print("Odd count: ", odd)

# Driver Code

# Given Dictionary
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

countEvenOdd(dict)
