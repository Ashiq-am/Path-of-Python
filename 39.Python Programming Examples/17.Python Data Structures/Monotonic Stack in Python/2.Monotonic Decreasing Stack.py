def monotonic_decreasing_stack(arr):
    # Initialize an empty stack to maintain the decreasing order
    stack = []

    # Iterate through each element in the input array
    for num in arr:
        # While the stack is not empty and the top of the stack is less than the current element
        while stack and stack[-1] < num:
            # Pop the top element from the stack
            stack.pop()
        # Push the current element onto the stack
        stack.append(num)

    # Return the stack, which now contains elements in monotonic decreasing order
    return stack


# Example usage
arr = [2, 1, 2, 4, 3]
print(monotonic_decreasing_stack(arr))
