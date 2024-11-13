# Python program to find the
# length of dictionary values

def main():
    # Defining the dictionary
    dict1 = {'A': "abcd",'B': set[1, 2, 3],'C':[12],'D': [1, 2, 4, 5, 5, 5]}

    # Create a empty dictionary
    dict2 = {}

    # using in operator
    for k in dict1:

        # Check the type of value
        # is int or not
        if isinstance(dict1[k], int):
            dict2[k] = 1

        # Check the type of value
        # is str or not
        elif isinstance(dict1[k], str):

            dict2[k] = 1

        else:
            dict2[k] = len(dict1[k])

    print("The length of values associated with their keys are:", dict2)
    print("The length of value associated with key 'B' is:", dict2['B'])



 # Driver Code
if __name__ == '__main__':
    main()
