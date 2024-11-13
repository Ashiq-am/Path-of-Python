num1 = "1110"
num2 = "0110"
print("num1:", num1, "and num2:", num2)

ans = int(num1, 2) - int(num2, 2)
print("The subtraction using int() function:", bin(ans)[2:])
