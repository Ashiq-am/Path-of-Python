# Program to cyclically rotate an array by one

def cyclicRotate(input):
    # slice list in two parts and append
    # last element in front of the sliced list

    # [input[-1]] --> converts last element pf array into list
    # to append in front of sliced list

    # input[0:-1] --> list of elements except last element
    print([input[-1]] + input[0:-1])


# Driver program
if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    cyclicRotate(input)
