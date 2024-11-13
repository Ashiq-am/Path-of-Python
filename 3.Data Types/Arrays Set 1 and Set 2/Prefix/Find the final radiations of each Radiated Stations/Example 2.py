# Python3 implementation of the approach

# Function to print the final radiations
def print_array(rStation, n):
    for i in range(1, n + 1):
        print(rStation[i], end=" ")


# Function to create the array of the
# resultant radiations
def radiated_Station(station, n):
    # Resultant radiations
    rStation = [0] * (n + 1)

    left_Rad = [0] * (n + 2)
    right_Rad = [0] * (n + 2)

    # Frequency of stations that
    # affect each station
    lCount = [0] * (n + 2)
    rCount = [0] * (n + 2)

    for i in range(1, n + 1):
        # Radiation of station i
        Rad = station[i]

        # Left and right most position of
        # radiation for station i, index
        # should be in between the station range
        li = max(1, i - Rad + 1)
        ri = min(n, Rad - 1 + i);

        # At station 1 radiation effect
        # for station i
        at1 = max(0, Rad - i + 1)
        left_Rad[1] += at1;

        # While iterating from left avoid
        # effective radiation at right
        left_Rad[i + 1] -= Rad;

        # At station n radiation effect
        # for station i
        atn = max(0, Rad - n + i);
        right_Rad[n] += atn

        # While iterating from right avoid
        # effective radiation at left
        right_Rad[i - 1] -= Rad

        # Left and right most position
        # where station i effects
        lCount[li] += 1
        rCount[ri] += 1

        # Avoiding right radiation for
        # left iteration and vice-versa
        lCount[i + 1] -= 1
        rCount[i - 1] -= 1

    # Left iteration
    for i in range(1, n + 1):
        lCount[i] += lCount[i - 1]

        # Total radiations at index 1
        # already counted
        if (i > 1):
            left_Rad[i] += (left_Rad[i - 1] +
                            lCount[i])

    # Right iteration
    for i in range(n, 0, -1):
        rCount[i] += rCount[i + 1]

        # Total radiations at index n already counted
        if (i < n):
            right_Rad[i] += (right_Rad[i + 1] +
                             rCount[i])

    # Final iteration that creates
    # the resultant radiation
    for i in range(1, n + 1):
        # Added extra value in each index
        rStation[i] = (left_Rad[i] +
                       right_Rad[i] -
                       station[i])

    # Print the resultant radiation
    # for each of the stations
    print_array(rStation, n)


# Driver code
if __name__ == "__main__":
    # 1-based indexing
    station = [0, 7, 9, 12, 2, 5]
    n = len(station) - 1

    radiated_Station(station, n)

# This code is contributed by chitranayal
