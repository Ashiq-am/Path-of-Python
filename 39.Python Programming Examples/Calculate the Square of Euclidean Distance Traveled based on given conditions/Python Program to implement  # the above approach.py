# Python Program to implement
# the above approach
def robotSim(commands, obstacles):
    # Possible movements in x coordinate.
    dx = [0, 1, 0, -1]

    # Possible movements in y coordinte.
    dy = [1, 0, -1, 0]

    # Initialise position to (0, 0).
    x, y = 0, 0

    # Initial direction is north.
    di = 0

    # Put all obstacles into hashmap.
    obstacleSet = set(map(tuple, obstacles))

    # maximum distance
    ans = 0

    # Iterate commands.
    for cmd in commands:

        # Left direction
        if cmd == -2:
            di = (di - 1) % 4

        # Right direction
        elif cmd == -1:
            di = (di + 1) % 4

        # If no direction changes
        else:
            for i in range(cmd):
                # Checking for obstacles.
                if (x + dx[di], y + dy[di]) \
                        not in obstacleSet:
                    # Update x coordinate
                    x += dx[di]

                    # Update y co ordinate
                    y += dy[di]

                    # Updating for max distance
                    ans = max(ans, x * x + y * y)
    print(ans)


# Driver Code
if __name__ == "__main__":
    commands = [4, -1, 4, -2, 4]
    obstacles = [[2, 4]]
    robotSim(commands, obstacles)
