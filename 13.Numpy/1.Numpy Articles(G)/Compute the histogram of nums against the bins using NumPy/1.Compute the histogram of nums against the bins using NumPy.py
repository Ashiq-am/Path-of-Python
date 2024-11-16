# Dataset
a = (1, 3, 7, 7, 2, 3, 4, 7, 6, 6, 3, 5, 2)

# Creating empty dictionary
hist = {}

# Counting the number of occurences
for i in a:
	hist[i] = hist.get(i, 0) + 1

# Printing the frequency table i.e histogram
print(hist)
