# Python program for the above approach

# Function to find the ranking of teams
def RankTeams(arr):
    # Traverse the list arr
    for i in range(len(arr)):

        # arr[i][0] is equal to arr[i][1]
        if (arr[i][0] == arr[i][1]):
            print("Invalid")
            return

        # Convert the goal to integer
        arr[i][2] = int(arr[i][2])
        arr[i][3] = int(arr[i][3])

    # Stores the list of GD, GA, and GF
    table = {}

    # Traverse the list
    for i in range(len(arr)):

        # Store the list of GA, GF
        # and GD of first team
        li1 = [0] * 4

        # Store the list of GA, GF
        # and GD of second team
        li2 = [0] * 4

        # If arr[i][0] is in table
        if arr[i][0] in table:
            li1 = table[arr[i][0]]

        # If arr[i][1] is in table
        if arr[i][1] in table:
            li2 = table[arr[i][1]]

        # Increment GF by arr[i][2]
        li1[2] += arr[i][2]

        # Increment GA by arr[i][3]
        li1[3] += arr[i][3]

        # Increment GF by arr[i][3]
        li2[2] += arr[i][3]

        # Increment GA by arr[i][2]
        li2[3] += arr[i][2]

        # Update GD
        li1[1] = li1[2] - li1[3]
        li2[1] = li2[2] - li2[3]

        # If tie
        if (arr[i][2] == arr[i][3]):
            li1[0] += 1
            li2[0] += 1

        # If arr[i][0] wins
        elif (arr[i][2] > arr[i][3]):
            li1[0] += 2

        # If arr[i][1] wins
        elif (arr[i][2] < arr[i][3]):
            li2[0] += 2

        # Update list in table
        table[arr[i][0]] = li1
        table[arr[i][1]] = li2

    # Traverse the sortd table in the given priority
    for key, value in sorted(table.items(),
                             key=lambda r: (-r[1][0],
                                            -r[1][1],
                                            -r[1][2],
                                            r[0])):
        # Print the team name
        print(key, end='\n')


# Driver Code

# Input
arr = [['Spain', 'England', '3', '0'],
       ['England', 'France', '1', '1'],
       ['Spain', 'France', '0', '2']]

RankTeams(arr)
