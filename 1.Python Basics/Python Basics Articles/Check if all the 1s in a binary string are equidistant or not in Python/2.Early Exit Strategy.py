def are_1s_equidistant_early_exit(s):
    # initialise previous index and distance
    prev_index = -1
    distance = None
    # iterate over the string
    for i, char in enumerate(s):
        if char == '1':
            # update previous index for the first occurence
            if prev_index == -1:
                prev_index = i
            else:
                # calculate current dustance
                current_distance = i - prev_index
                # update distance for the first occurence
                if distance is None:
                    distance = current_distance
                # compare distance with current distance
                elif distance != current_distance:
                    return False
                # update previous index
                prev_index = i
    return True

s = "1001001010100100"
print(are_1s_equidistant_early_exit(s))
