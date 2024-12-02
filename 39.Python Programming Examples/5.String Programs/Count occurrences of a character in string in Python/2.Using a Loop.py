s = "hello world"

# Define target character to count
target = 'l'

# Initialize a counter to keep track of occurrences
count = 0

# Iterate over each character in the string
for c in s:

    # Check if current character matches target
    if c == target:
        # Increment count if there's a match
        count += 1

print(count)