# Python program to remove random elements of choice
# Function to remove elements using discard()
def Remove(sets):
    sets.discard(20)
    print(sets)


# Driver Code
sets = set([10, 20, 26, 41, 54, 20])
Remove(sets)


