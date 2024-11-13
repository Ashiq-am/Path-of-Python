# Python program to find the
# length of dictionary values


def main():
    # Defining the dictionary
    dict1 = {'A': "abcd",
             'B': set([1, 2, 3]),
             'C': (12, "number"),
             'D': [1, 2, 4, 5, 5, 5]}

    # using dictionary comprehension
    dict2 = {k: 1 if isinstance(dict1[k], (str, int))
    else len(dict1[k])
             for k in dict1}

    print("The length of values associated \
    with their keys are:", dict2)
    print("The length of value associated \
    with key 'B' is:", dict2['B'])

    # Driver Code
    if __name__ == '__main__':
        main()
