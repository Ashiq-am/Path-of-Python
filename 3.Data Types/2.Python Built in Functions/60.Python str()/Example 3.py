# Python program to demonstrate
# str()

a = bytes("ŽString", encoding = 'utf-8')
s = str(a, encoding = "ascii", errors ="ignore")
print(s)
