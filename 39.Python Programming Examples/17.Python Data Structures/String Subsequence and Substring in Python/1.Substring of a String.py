# Python program to generate all substrings of a given string

def substrings(s):
    all_substrings = []
    n = len(s)  # Length of the string

    # Set the starting index of the substring
    for i in range(n):
        # Set the ending index of the substring
        for j in range(i + 1, n + 1):
            # Append the substring s[i:j] to the list
            all_substrings.append(s[i:j])

    return all_substrings


if __name__ == "__main__":
    input_string = "abc"

    # Get all substrings
    substrings_list = substrings(input_string)

    # Print all the substrings
    print("All substrings:")
    for substring in substrings_list:
        print(substring, end = " ")
