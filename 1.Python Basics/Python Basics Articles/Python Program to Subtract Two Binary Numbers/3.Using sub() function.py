from operator import *

num1 = "1110"
num2 = "0110"
print("num1:", num1, "and num2:", num2)

ans = sub(int(num1, 2), int(num2, 2))
print("The subtraction using sub() function:", bin(ans)[2:])
