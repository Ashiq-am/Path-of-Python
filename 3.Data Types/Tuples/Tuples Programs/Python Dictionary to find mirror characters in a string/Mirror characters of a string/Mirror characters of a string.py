# python code to find the reverse
# alphabetical order from a given
# position

# Function which take the given string and the
# position from which the reversing shall be
# done and returns the modified string
def compute(st, n):
    # Creating a string having reversed
    # alphabetical order
    reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
    l = len(st)

    # The string up to the point specified in the
    # question, the string remains unchanged and
    # from the point up to the length of the
    # string, we reverse the alphabetical order
    answer = ""
    for i in range(0, n):
        answer = answer + st[i]

    for i in range(n, l):
        answer = (answer +
                  reverseAlphabet[ord(st[i]) - ord('a')]);

    return answer


# Driver function
st = "pneumonia"
n = 4
answer = compute(st, n - 1)
print(answer)
