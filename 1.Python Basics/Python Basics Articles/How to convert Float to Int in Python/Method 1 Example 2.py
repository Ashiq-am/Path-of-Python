# example of unpredictable
# behaviour of int()

num1 = 5.9
num2 = 5.99999999999999999999

num1 = int(num1)
num2 = int(num2)

print(num1, num2, sep = '\n')
