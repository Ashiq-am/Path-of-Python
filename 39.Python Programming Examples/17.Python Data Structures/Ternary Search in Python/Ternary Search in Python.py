def ternary_search(func, left, right, absolute_precision=1e-9):
    """
    Perform ternary search to find the maximum value of a unimodal function within the given range.

    Parameters:
        func (callable): The unimodal function to be maximized.
        left (float): The left endpoint of the search range.
        right (float): The right endpoint of the search range.
        absolute_precision (float): The absolute precision used for termination (default: 1e-9).

    Returns:
        float: The x-coordinate of the maximum value within the given range.
    """
    while right - left > absolute_precision:
        mid1 = left + (right - left) / 3
        mid2 = right - (right - left) / 3
        if func(mid1) < func(mid2):
            left = mid1
        else:
            right = mid2
    return (left + right) / 2

# Example usage:
def f(x):
    return -(x - 3) ** 2 + 5  # Example unimodal function

max_x = ternary_search(f, 0, 5)  # Searching within the range [0, 5]
max_y = f(max_x)
print("Maximum value at x =", max_x, "with y =", max_y)
