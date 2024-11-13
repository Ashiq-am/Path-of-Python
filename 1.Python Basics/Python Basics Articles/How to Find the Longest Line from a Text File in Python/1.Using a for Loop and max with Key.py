with open('file.txt', 'r') as file:
    longest_line = max(file, key=len)

print("Longest line:", longest_line)
