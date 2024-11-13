# string creation
str = "GFG Learning-Portal"

for i in str:
	print(i, end="")

print()
for i in range(0, len(str), 2):
	print(str[i], end="_")
