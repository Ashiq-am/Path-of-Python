# function to solve all the static range queries
def solve(arr, queries):
    # Creating a prefix Sum Array
    prefix_sum = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    # Creating Result array to store the result of each query
    result = []
    for query in queries:
        l, r = query[0], query[1]
        # Calculating sum for the current query range
        sum_val = prefix_sum[r] - prefix_sum[l - 1]
        result.append(sum_val)
    return result

# Sample Input
arr = [3, 2, 4, 5, 1, 1, 5, 3]
queries = [[2, 4], [5, 6], [1, 8], [3, 3]]

# Function Call
result = solve(arr, queries)
for sum_val in result:
    print(sum_val, end=" ")
print()
