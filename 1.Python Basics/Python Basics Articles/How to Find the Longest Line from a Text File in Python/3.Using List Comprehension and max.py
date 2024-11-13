with open('file.txt', 'r') as file:
    lines = [line for line in file]
    longest_line = max(lines, key=len)

print("Longest line:", longest_line)
