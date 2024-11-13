# Python program to find the
# length of dictionary values


def main():
    # Defining the dictionary
    dict1 = {'a': [1, 2, 3],'b': (1, 2, 3),'c': 5,'d': "nopqrs",'e': ["A", "B", "C"]}

    # using list comprehension
    count = sum([1 if isinstance(dict1[k], (str, int))
                 else len(dict1[k])
                 for k in dict1])

    print("The total length of values is:", count)

    # Driver Code
    if __name__ == '__main__':
        main()
