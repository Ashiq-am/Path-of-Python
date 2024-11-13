def subtraction(num1, num2):
	return num1 + (~num2 + 1)

num1 = "1110"
num2 = "0110"
print("num1:", num1, "and num2:", num2)
ans = subtraction(int(num1, 2), int(num2, 2))
print("The subtraction using 2's Complement:", bin(ans))
