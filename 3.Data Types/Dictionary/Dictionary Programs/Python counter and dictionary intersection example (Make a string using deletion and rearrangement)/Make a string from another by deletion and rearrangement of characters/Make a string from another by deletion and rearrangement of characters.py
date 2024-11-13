# Python 3 program to find if it is possible
# to make a string from characters present
# in other string.
MAX_CHAR = 256


# Returns true if it is possible to make
# s1 from characters present in s2.
def isPossible(s1, s2):
    # Count occurrences of all characters
    # present in s2..
    count = [0] * MAX_CHAR
    for i in range(len(s2)):
        count[ord(s2[i])] += 1

    # For every character, present in s1,
    # reduce its count if count is more
    # than 0.
    for i in range(len(s1)):
        if (count[ord(s1[i])] == 0):
            return False
        count[ord(s1[i])] -= 1

    return True


# Driver code
if __name__ == "__main__":

    s1 = "GeeksforGeeks"
    s2 = "rteksfoGrdsskGeggehes"
    if (isPossible(s1, s2)):
        print("Possible")
    else:
        print("Not Possible")
