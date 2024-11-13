# Assign matrix
twoDMatrix = [[10, 20, 30],
			[40, 50, 60],
			[70, 80, 90]]

# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]

print(trans)
