# Python 3 program to find two disjoint
# good sets of vertices in a given graph
N = 100005

# For the graph
gr = [[] for i in range(N)]
dis = [[] for i in range(2)]
vis = [False for i in range(N)]
colour = [0 for i in range(N)]
bip = 0


# Function to add edge
def Add_edge(x, y):
    gr[x].append(y)
    gr[y].append(x)


# Bipartite function
def dfs(x, col):
    vis[x] = True
    colour[x] = col

    # Check for child vertices
    for i in gr[x]:

        # If it is not visited
        if (vis[i] == False):
            dfs(i, col ^ 1)

        # If it is already visited
        elif (colour[i] == col):
            bip = False


# Function to find two disjoint
# good sets of vertices in a given graph
def goodsets(n):
    # Initially assume that
    # graph is bipartite
    bip = True

    # For every unvisited vertex call dfs
    for i in range(1, n + 1, 1):
        if (vis[i] == False):
            dfs(i, 0)

    # If graph is not bipartite
    if (bip == 0):
        print(-1)
    else:

        # Differentiate two sets
        for i in range(1, n + 1, 1):
            dis[colour[i]].append(i)

        # Print vertices belongs to both sets
        for i in range(2):
            for j in range(len(dis[i])):
                print(dis[i][j], end=" ")
            print('\n', end="")


# Driver code
if __name__ == '__main__':
    n = 6
    m = 4

    # Add edges
    Add_edge(1, 2)
    Add_edge(2, 3)
    Add_edge(2, 4)
    Add_edge(5, 6)

    # Function call
    goodsets(n)

# This code is contributed
# by Surendra_Gangwar
