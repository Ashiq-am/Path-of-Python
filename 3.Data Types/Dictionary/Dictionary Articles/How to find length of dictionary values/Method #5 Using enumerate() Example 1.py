# Python program to find the
# length of dictionary values

def main():
    # Defining the dictionary
    dict1 = {'a': [1, 2, 3],'b':(1, 2, 3),'c': 5,'d': "nopqrs",'e': ["A", "B", "C"]}

    # Initialize count
    count = 0

    # using enumerate()
    for k in enumerate(dict1.items()):

        # Check the type of value
        # is int or not
        if isinstance(k[1][1], int):
            count += 1


        # Check the type of value
        # is str or not
        elif isinstance(k[1][1], str):
            count += 1



        else:
            count += len(k[1][1])


    print("The total length of value is:", count)




# Driver Code
if __name__ == '__main__':
    main()
