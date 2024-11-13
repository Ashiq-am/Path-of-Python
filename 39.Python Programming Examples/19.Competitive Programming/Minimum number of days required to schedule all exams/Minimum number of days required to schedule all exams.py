# Python 3 program for the above approach

# Comparator function to sort the
# vector of pairs in decreasing order

# Function to add an undirected
# edge between any pair of nodes
def addEdge(adj, u, v):
    adj[u][v] = 1
    adj[v][u] = 1


# Function to find the minimum number
# of days to schedule all the exams
def minimumDays(V, Edges, E):
    # Stores the adjacency list of
    # the given graph
    adj = [[0 for i in range(V)] for j in range(V)]

    # Iterate over the edges
    for i in range(E):
        u = Edges[i][0]
        v = Edges[i][1]

        # Add the edges between the
        # nodes u and v
        addEdge(adj, u, v)

    # Initialize a vector of pair that
    # stores [degree, vertex }
    vdegree = [[0, 0] for i in range(V)]

    for i in range(V):
        # Degree of the node
        degree = 0
        vdegree[i][1] = i

        for j in range(V):
            if (adj[i][j] != 0):
                # Increment the degree
                degree += 1

        # Update the degree of the
        # current node
        vdegree[i][0] = degree

    # Sort to arrange all vertices
    # in descending order of degree
    vdegree.sort(reverse=True)

    # Stores the vertices according
    # to degree in descending order
    vorder = [0 for i in range(V)]

    for i in range(V):
        vorder[i] = vdegree[i][1]

    # Stores the color of the all
    # the nodes
    color = [0 for i in range(V)]

    for i in range(V):
        color[i] = i + 1

    colored = [0 for i in range(V)]

    # Keeps the track of number of
    # vertices colored
    numvc = 0

    # Track the different color
    # assigned
    k = 0

    for i in range(V):
        # If all vertices are colored
        # then exit from the for loop
        if (numvc == V):
            break

        # If vertex is already
        # colored, then continue
        if (colored[vorder[i]] != 0):
            continue

        # If vertex not colored
        else:
            colored[vorder[i]] = color[k]

            # After coloring increase
            # the count of colored
            # vertex by 1
            numvc += 1

            for j in range(V):
                # If the current node
                # and its adjacent are
                # not colored
                if (colored[j] == 0 and adj[vorder[i]][j] == 0):
                    colored[j] = color[k]

                    # Increment the count
                    numvc += 1

            # Increment k
            k += 1

    # Sort the array
    colored.sort()

    # Count of unique colors
    unique_color = 1

    # Count the number of unique
    # colors
    for i in range(1, V, 1):
        if (colored[i] != colored[i - 1]):
            unique_color += 1

    # Return the number of days
    # to sechedule an exam
    return unique_color


# Driver Code
if __name__ == '__main__':
    V = 7
    E = 12
    Edges = [[0, 1], [0, 3], [0, 4], [0, 6], [1, 2], [1, 4], [1, 6], [2, 5], [2, 6], [3, 4], [3, 5], [4, 5]]
    print(minimumDays(V, Edges, E))

# This code is contributed by ipg2016107.
