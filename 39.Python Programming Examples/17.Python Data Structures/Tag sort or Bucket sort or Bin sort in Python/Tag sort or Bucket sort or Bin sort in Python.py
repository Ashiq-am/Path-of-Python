def tag_sort(arr):
    """
    Perform tag sort to sort the elements of the array.

    Parameters:
        arr (list): The input list to be sorted.

    Returns:
        list: The sorted list.
    """
    max_val = max(arr)
    min_val = min(arr)
    tag_range = max_val - min_val + 1

    # Create tags as empty lists
    tags = [[] for _ in range(tag_range)]

    # Place each element into its corresponding tag
    for num in arr:
        tags[num - min_val].append(num)

    # Concatenate elements of all tags
    sorted_arr = []
    for tag in tags:
        sorted_arr.extend(tag)

    return sorted_arr

# Example usage:
arr = [4, 3, 6, 1, 2, 5, 9, 8, 7]
sorted_arr = tag_sort(arr)
print("Sorted array:", sorted_arr)
