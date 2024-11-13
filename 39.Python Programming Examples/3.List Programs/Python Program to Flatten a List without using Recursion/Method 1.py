# Input list
l = [1, 2, [3, 4, [5, 6], 7],
     [[[8, 9], 10]],
     [11, [12, 13]]]


# Function to flatten the the list


def flatten(input_list):
    # Final list to be returned
    result = []

    # Creating stack and adding
    # all elements into it
    stack = [input_list]

    # Iterate stack till it
    # does not get empty
    while stack:

        # Get the last element of the stack
        current = stack.pop(-1)

        # If the last element is a list,
        # add all the elements of that list in stack
        if isinstance(current, list):
            stack.extend(current)

        # Else add that element in the result
        else:
            result.append(current)

    # Reverse the result to get the
    # list in original order
    result.reverse()

    return result


# output list
ans = flatten(l)
print(ans)
