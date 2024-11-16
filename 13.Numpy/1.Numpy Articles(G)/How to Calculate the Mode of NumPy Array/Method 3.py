# creating a list
lst = [1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 5, 5, 5]


# defining a function to calulate mode. It
# takes list variable as argument
def mode(lst):
    # creating a dictionary
    freq = {}
    for i in lst:
        # mapping each value of list to a
        # dictionary
        freq.setdefault(i, 0)
        freq[i] += 1

    # finding maximun value of dictionary
    hf = max(freq.values())

    # creating an empty list
    hflst = []

    # using for loop we are checking for most
    # repeated value
    for i, j in freq.items():
        if j == hf:
            hflst.append(i)

    # returning the result
    return hflst


# calling mode() function and passing list
# as argument
print(mode(lst))
