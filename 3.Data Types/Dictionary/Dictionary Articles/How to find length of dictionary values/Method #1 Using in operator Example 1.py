# Python program to find the
# length of dictionary values


def main():
    # Defining the dictionary
    dict1 = {'a': [1, 2, 3],'b':[1, 2, 3],'c': [5],'d': ["nopqrs"],'e': ["A", "B", "C"]}

    # Initialize count
    count = 0

    # using in operator
    for k in dict1:

        # Check the type of value
        # is int or not
        if isinstance(dict1[k], int):
            count += 1

            # Check the type of value
            # is str or not
        elif isinstance(dict1[k], str):

            count += 1


        else:
            count += len(dict1[k])

    print("The total length of value is:", count)


# Driver Code


if __name__ == '__main__':
    main()
