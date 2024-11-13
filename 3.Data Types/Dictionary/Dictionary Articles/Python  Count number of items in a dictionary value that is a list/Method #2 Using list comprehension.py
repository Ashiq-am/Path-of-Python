# Python program to count number of items
# in a dictionary value that is a list.
def main():
    # defining the dictionary
    d = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
         'B': 34,
         'C': 12,
         'D': [7, 8, 9, 6, 4]}

    # using list comprehension
    print(sum([len(d[x]) for x in d if isinstance(d[x], list)]))


if __name__ == '__main__':
    main()
