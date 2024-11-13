# Python3 Program to count even and
# odd numbers present in a dictionary

# Function to count even and odd
# numbers present in a dictionary
def countEvenOdd(dict):
    # Stores count of even
    # and odd elements
    even = 0
    odd = 0

    # Traverse the dictionary
    for i in dict.values():

        if i % 2 == 0:
            even = even + 1

        else:
            odd = odd + 1

    print("Even Count: ", even)
    print("Odd Count: ", odd)


# Driver Code

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
countEvenOdd(dict)
