def are_1s_equidistant(s):
    # Find positions of 1s
    positions = [i for i, char in enumerate(s) if char == '1']

    # Check if less than 2 1s
    if len(positions) < 2:
        return True

    # Calculate distance
    distance = positions[1] - positions[0]

    # Iterate over remaining 1s
    for i in range(2, len(positions)):
        #  Compare distances
        if positions[i] - positions[i - 1] != distance:
            return False

    return True


s = "100100100100100"
print(are_1s_equidistant(s))
