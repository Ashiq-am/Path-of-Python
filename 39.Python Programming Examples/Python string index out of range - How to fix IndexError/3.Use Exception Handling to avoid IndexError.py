s = 'GeeksforGeeks'

# valid index range is 0 to 12
index = 13

try:
    print("Character at index:", s[index])
except IndexError:
    print("Index out of range!")