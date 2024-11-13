# Function which returns last word
def lastWord(string):
    # taking empty string
    newstring = ""

    # calculating length of string
    length = len(string)

    # traversing from last
    for i in range(length - 1, 0, -1):

        # if space is occured then return
        if (string[i] == " "):

            # return reverse of newstring
            return newstring[::-1]
        else:
            newstring = newstring + string[i]

        # Driver code


string = "Learn algorithms at geeksforgeeks"
print(lastWord(string))
