# Python program to print all subsequences of a string


def print_subsequences(s, subseq="", index=0):
    # Function to print all subsequences of a string.

    if index == len(s):
        # Print the current subsequence
        print(subseq, end=" ")
        return

    # Include the character at the current index
    # in the subsequence
    print_subsequences(s, subseq + s[index], index + 1)

    # Exclude the character at the current index
    # from the subsequence
    print_subsequences(s, subseq, index + 1)


if __name__ == "__main__":
    print("All Subsequences:")
    input_string = "abc"
    print_subsequences(input_string)
