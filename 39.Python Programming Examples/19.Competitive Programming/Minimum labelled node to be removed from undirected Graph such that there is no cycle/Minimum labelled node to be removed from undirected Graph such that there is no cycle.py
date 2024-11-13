# Python3 implementation to find the
# minimum labelled node to be
# removed such that there is no
# cycle in the undirected graph
MAX = 100005;
totBackEdges = 0
countAdj = [0 for i in range(MAX)]
small = [0 for i in range(MAX)]

# Variables to store if a node V has
# at-most one back edge and store the
# depth of the node for the edge
isPossible = [0 for i in range(MAX)]
depth = [0 for i in range(MAX)]
adj = [[] for i in range(MAX)]
vis = [0 for i in range(MAX)]


# Function to swap the pairs of the graph
def change(p, x):
    # If the second value is
    # greater than x
    if (p[1] > x):
        p[1] = x;

    # Put the pair in the ascending
    # order internally
    if (p[0] > p[1]):

    tmp = p[0];
    p[0] = p[1];
    p[1] = tmp;


# Function to perform the DFS
def dfs(v, p=-1, de=0):
    global vis, totBackEdges

    # Initialise with the large value
    answer = [100000000, 100000000]

    # Storing the depth of this vertex
    depth[v] = de;

    # Mark the vertex as visited
    vis[v] = 1;
    isPossible[v] = 1;

    # Iterating through the graph
    for u in adj[v]:

        # If the node is a child node
        if ((u ^ p) != 0):

            # If the child node is unvisited
            if (vis[u] == 0):

                # Move to the child and increase
                # the depth
                x = dfs(u, v, de + 1);

                # increase according to algorithm
                small[v] += small[u];

                change(answer, x[1]);
                change(answer, x[0]);

                # If the node is not having
                # exactly K backedges
                if (x[1] < de):
                    isPossible[v] = 0;

            # If the child is already visited
            # and in current dfs
            # (because colour is 1)
            # then this is a back edge
            elif (vis[u] == 1):
                totBackEdges += 1

                # Increase the countAdj values
                countAdj[v] += 1
                countAdj[u] += 1
                small[p] += 1
                small[u] -= 1
                change(answer, depth[u]);

    # Colour this vertex 2 as
    # we are exiting out of
    # dfs for this node
    vis[v] = 2;
    return answer;


# Function to find the minimum labelled
# node to be removed such that
# there is no cycle in the undirected graph
def minNodetoRemove(n, edges):
    # Construct the graph
    for i in range(len(edges)):
        adj[edges[i][0]].append(edges[i][1]);
        adj[edges[i][1]].append(edges[i][0]);

    global vis, totBackEdges

    # Mark visited as false for each node
    vis = [0 for i in range(len(vis))]
    totBackEdges = 0;

    # Apply dfs on all unmarked nodes
    for v in range(1, n + 1):
        if (vis[v] == 0):
            dfs(v);

    # If no backedges in the initial graph
    # this means that there is no cycle
    # So, return -1
    if (totBackEdges == 0):
        return -1;
    node = -1;

    # Iterate through the vertices and
    # return the first node that
    # satisfies the condition
    for v in range(1, n + 1):

        # Check whether the count sum of
        # small[v] and count is the same as
        # the total back edges and
        # if the vertex v can be removed
        if ((countAdj[v] + small[v] == totBackEdges) and isPossible[v] != 0):
            node = v;
        if (node != -1):
            break;
    return node;


# Driver code
if __name__ == '__main__':
    N = 5;
    edges = []
    edges.append([5, 1]);
    edges.append([5, 2]);
    edges.append([1, 2]);
    edges.append([2, 3]);
    edges.append([2, 4]);
    print(minNodetoRemove(N, edges));

# This code is contributed by Pratham76
