# Using a dictionary to count words
s = "Geeks for Geeks"
word = s.split()
count = {}

for i in word:
    count[i] = count.get(i, 0) + 1

print(count)