# Python program to find the
# length of dictionary values

def main():
    # Defining the dictionary
    dict1 = {'a': [1, 2, 3],'b':(1, 2, 3),'c': 5,'d': "nopqrs",'e': ["A", "B", "C"]}

    # Initialize count
    count = 0

    # using dict.items()
    for key, val in dict1.items():

        # Check the type of value
        # is int or not
        if isinstance(val, int):
            count += 1

            # Check the type of value
            # is str or not
        elif isinstance(val, str):
            count += 1

        else:
            count += len(val)
    print("The total length of value is:", count)



# Driver code

if __name__ == '__main__':
    main()
