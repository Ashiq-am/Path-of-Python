# Python3 program to Reverse order
# of incrementing integers in list

def reverseOrder(lst):
    res = []
    block = []
    for i in lst:

        # check if the current element is less
        # than the last element of block
        if block and i < block[-1]:

            # add reversed chunk to 'res'
            res.extend(block[::-1])
            block[:] = [i]
        else:

            # append the element to 'block'
            block.append(i)

    # extend 'res' by reversing block
    res.extend(block[::-1])
    return (res)


# Driver code
lst = [0, 1, 9, 8, 7, 5, 3, 14]
print(reverseOrder(lst))
