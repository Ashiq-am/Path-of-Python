# Function to find the minimum element using Brute Force
def brute_force_rmq(arr, start, end):
    result = arr[start]
    for i in range(start + 1, end + 1):
        result = min(result, arr[i])
    return result


# Example usage:
arr = [5, 2, 7, 1, 9, 4, 3]
start, end = 1, 4
print("Minimum within the range [1, 4]:", brute_force_rmq(arr, start, end))
