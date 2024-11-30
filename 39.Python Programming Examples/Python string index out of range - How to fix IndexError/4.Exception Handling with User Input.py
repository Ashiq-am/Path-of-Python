s = 'GeeksforGeeks'

index = int(input("Enter an index: "))
# Example: User enters 13 [which is invalid index]

try:
    print("Character at index:", s[index])
except IndexError:
    print("Index out of range! Please enter a valid index.")