# Python3 code to find all possible substrings that
# are also the prefix of the given string

# Function to print all the special substrings
def func(string):
    # Used to store the starting and
    # ending index of the substrings
    start, end = 0, 0

    while start < len(string):

        # If substring is also the prefix
        if string[end] == string[end - start]:

            # Print the substring
            print(string[start:end + 1], end=" ")
            end += 1

            if end == len(string):
                start += 1
                end = start

            # Increment the starting
        # index of the substring
        else:
            start += 1
            end = start


if __name__ == "__main__":
    string = "ababc"
    func(string)
