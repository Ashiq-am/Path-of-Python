# code
def binary_to_decimal(binary):
	decimal = 0
	power = len(binary) - 1
	for digit in binary:
		decimal += int(digit) * (2 ** power)
		power -= 1
	return decimal

def decimal_to_binary(decimal):
	binary = ""
	while decimal > 0:
		remainder = decimal % 2
		binary = str(remainder) + binary
		decimal = decimal // 2
	return binary


num1 = "1110"
num2 = "0110"

print("num1:", num1, "and num2:", num2)

a = binary_to_decimal(num1)
b = binary_to_decimal(num2)

# The resultant difference of decimal numbers
temp = a - b

# converting the subtraction output back to binary
ans = decimal_to_binary(temp)

print("The subtraction result is:", ans)
