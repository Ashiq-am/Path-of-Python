# Python program to find the
# length of dictionary values

def main():
    # Defining the dictionary
    dict1 = {'A': "abcd",
             'B': set([1, 2, 3]),
             'C': (12, "number"),
             'D': [1, 2, 4, 5, 5, 5]}

    # Create a empty dictionary
    dict2 = {}

    # using enumerate()
    for k in enumerate(dict1.items()):

        # Check the type of value
        # is int or not
        if isinstance(k[1][1], int):
            dict2[k[1][0]] = 1

        # Check the type of value
        # is str or not
        elif isinstance(k[1][1], str):
            dict2[k[1][0]] = 1

        else:
            dict2[k[1][0]] = len(k[1][1])

    print("The length of values associated\
    with their keys are:", dict2)

    print("The length of value associated \
    with key 'B' is:", dict2['B'])

    # Driver Code
    if __name__ == '__main__':
        main()
