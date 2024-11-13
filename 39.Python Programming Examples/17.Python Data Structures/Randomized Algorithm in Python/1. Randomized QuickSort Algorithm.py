def quicksort(arr):
    """
    Sorts an array using the randomized Quicksort algorithm.
    """

    # 1. Base case: If the array has 1 or fewer elements, it's already sorted.
    if len(arr) <= 1:
        return arr

    # 2. Choose a random pivot element from the array.
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # 3. Partition the array around the pivot:
    #   - Create three sub-arrays: left (elements less than pivot),
    # middle (elements equal to pivot), and right (elements greater than pivot).
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 4. Recursively sort the left and right sub-arrays.
    return quicksort(left) + middle + quicksort(right)
