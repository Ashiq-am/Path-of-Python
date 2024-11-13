# Buttons
radius = 24
space = 20
letters = [] # [399, 122, "A", True]
x_start = round((WIDTH - (radius * 2 + space) * 13) / 2)
y_start = 540

A = 65 # Using ASCII value to print letters on the button. A->65, B->66, and so on

for i in range(26):
	x = x_start + space * 2 + ((radius * 2 + space) * (i % 13))
	y = y_start + ((i // 13) * (space + radius * 2))
	letters.append([x, y, chr(A + i), True])
