# Python 3 implementation of the approach

# Function to print the final radiations
def printf(rStation, n):
    for i in range(1, n + 1, 1):
        print(rStation[i], end=" ")
    print("\n", end=" ")


# Function to create the array of the
# resultant radiations
def radiated_Station(station, n):
    # Resultant radiations
    rStation = [0 for i in range(n + 1)]

    for i in range(1, n + 1):
        # Declaring index counter for left
        # and right radiation
        li = i - 1
        ri = i + 1

        # Effective radiation for left
        # and right case
        lRad = station[i] - 1
        rRad = station[i] - 1

        # Radiation for i-th station
        rStation[i] += station[i]

        # Radiation increment for left stations
        while (li >= 1 and lRad >= 1):
            rStation[li] += lRad
            lRad -= 1
            li -= 1

        # Radiation increment for right stations
        while (ri <= n and rRad >= 1):
            rStation[ri] += rRad
            rRad -= 1
            ri += 1

    # Print the resultant radiation
    # for each of the stations
    printf(rStation, n)


# Driver code
if __name__ == '__main__':
    # 1-based indexing
    station = [0, 7, 9, 12, 2, 5]
    n = len(station) - 1

    radiated_Station(station, n)

# This code is contributed by
# Surendra_Gangwar
