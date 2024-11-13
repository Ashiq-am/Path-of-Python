# Python3 program for the above approach

# Function to count the minimum number
# of tiles that gets cut by a single
# vertical strike of a sword
def cutTiles(tilesStack):
    # Map prefix sum of each row
    # of tilesStack
    gaps = {}

    # Handling the case when
    # map will be empty
    gaps[-1] = 0

    # Traverse each row of the tiles
    for tiles in tilesStack:

        # Stores distance of gap from
        # left of each row
        totWidth = 0

        # Excluding the last gap as it will
        # be the edge of the level
        for tile in tiles[:-1]:

            # Update totWidth
            totWidth += tile

            # If gap is already found at
            # this points in previous levels
            if totWidth in gaps:
                gaps[totWidth] += 1
            else:
                gaps[totWidth] = 1

    # Stores maximum number of
    # gap from left
    X = max(list(gaps.values()))

    print(len(tilesStack) - X)


# Driver Code
if __name__ == '__main__':
    tilesStack = [[2, 3], [3, 2], [1, 1, 1, 2],
                  [1, 1, 1, 1, 1]]

    # Function Call
    cutTiles(tilesStack)
