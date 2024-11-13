# Python code to get length of each words
def Cal_len(string):
    # Using splitlines() divide into a list
    li = string.splitlines()
    print(li)

    # Calculate length of each word
    l = [len(element) for element in li]
    return l


# Driver Code
string = "Welcome\rto\rGeeksforGeeks"
print(Cal_len(string))
