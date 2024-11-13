def tupleLargest(num_tuple, index=0, max_item=float("-inf")):
    # setting base condition for recursion
    if index == len(num_tuple):
        return max_item

    # getting item at current index
    current_item = num_tuple[index]

    # update if new greater value is found
    if current_item > max_item:
        max_item = current_item

    # recursive call with incremented index value
    return tupleLargest(num_tuple, index + 1, max_item)


if __name__ == '__main__':
    maxTuple = (11, 65, 54, 23, 76, 33, 82, 98)
    print("Tuple Items = ", maxTuple)

    largest_element = tupleLargest(maxTuple)
    print("Maximum Item in Tuple = ", largest_element)
