# Python implementation
# of the above approach

# Function to print uncommon digits
# of two numbers in descending order
def disticntUncommonDigits(A, B):
    # Stores digits of A as string
    A = str(A)

    # Stores digits of B as string
    B = str(B)

    # Stores the characters
    # of A in a integer list
    lis1 = list(map(int, A))

    # Stores the characters
    # of B in a integer list
    lis2 = list(map(int, B))

    # Converts lis1 to set
    lis1 = set(lis1)

    # Converts lis2 to set
    lis2 = set(lis2)

    # Stores the uncommon digits present
    # in the sets lis1 and lis2
    lis = lis1.symmetric_difference(lis2)

    # Converts lis to list
    lis = list(lis)

    # Sort the list in descending order
    lis.sort(reverse=True)

    # Print the list lis
    for i in lis:
        print(i, end=" ")


# Driver Code


# Input
A = 378212
B = 78124590

disticntUncommonDigits(A, B)
