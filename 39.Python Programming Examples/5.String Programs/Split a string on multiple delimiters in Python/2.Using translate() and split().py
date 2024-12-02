s = "apple, banana; orange grape"

# Replace delimiters with a space and split
s = s.translate(str.maketrans({',': ' ', ';': ' '}))
res = s.split()
print(res)