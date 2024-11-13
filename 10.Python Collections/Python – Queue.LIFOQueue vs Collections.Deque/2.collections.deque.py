# Import required modules
import collections

# Initialize deque
Deque = collections.deque([10, 20, 30])

# Using append() to insert element at right end
# Inserts 0 at the end of deque
Deque.append(0)

# Printing modified deque
print("The deque after appending at right is:", Deque)

# Using appendleft() to insert element at left end
# Inserts 100 at the beginning of deque
Deque.appendleft(100)

# Printing modified deque
print("The deque after appending at left is: ", Deque)


# Using pop() to delete element from right end
# Deletes 0 from the right end of deque
Deque.pop()

# Printing modified deque
print("The deque after deleting from right is:", Deque);

# Using popleft() to delete element from left end
# Deletes 100 from the left end of deque
Deque.popleft()

# Printing modified deque
print("Queue:", Deque)
