# Python program to remove random elements of choice
# Function to remove elements using remove()
def Remove(sets):
    sets.remove("gaurav")
    print(sets)


# Driver Code
sets = set(["ram", "aakash", "kaushik", "anand", "prashant"])
Remove(sets)
