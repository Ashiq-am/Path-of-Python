# Python Program to implement
# the above approach

# Function to split the input
# string into a list
def tokenizer(Str):
    List = Str.split()
    return List


# Function to sort the given list based
# on values at odd indices of the list
def SortListByOddIndices(List, x):
    l = len(List)

    # Function to remove the values
    # less than the given value x
    for i in range(l - 1, 0, -2):
        if int(List[i]) < x:
            del (List[i - 1: i + 1])

    l = len(List)

    for i in range(1, l, 2):
        for j in range(1, l - i, 2):

            # Compares values at odd indices of
            # the list to sort the list
            if List[j] < List[j + 2] \
                    or (List[j - 1] > List[j + 1] and List[j] == List[j + 2]):

                List[j], List[j + 2] = List[j + 2], List[j]

                List[j - 1], List[j + 1] = List[j + 1], List[j - 1]

    return ' '.join(List)


# Driver Code
Str = "Axc 78 Czy 60"
x = 77

# Function call
List = tokenizer(Str)

Str = SortListByOddIndices(List, x)

print(Str)
