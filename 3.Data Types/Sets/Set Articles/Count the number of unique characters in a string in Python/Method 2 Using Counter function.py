# Python program for the above approach
from collections import Counter


# Function to count the number of distinct
# characters present in the string str
def countDis(str):
    # Stores all frquencies
    freq = Counter(str)

    # Return the size of the freq dictionary
    return len(freq)


# Driver Code
if __name__ == "__main__":
    # Given string S
    S = "geeksforgeeks"

    print(countDis(S))
