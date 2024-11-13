# Using above second method to create a
# 2D array
rows, cols = (5, 5)
arr=[]
for i in range(cols):
	col = []
	for j in range(rows):
		col.append(0)
	arr.append(col)
print(arr)
