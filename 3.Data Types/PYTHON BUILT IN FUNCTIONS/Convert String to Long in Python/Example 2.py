a='0x'
arr0 = '00000018000004000000000000000000'
arr1 = '00000000000000000000000000000000'
arr2 = 'fe000000000000000000000000000000'
arr3 = '00000000000000000000000000ffffff'
data = a+arr0+arr1+arr2+arr3
print(data)
print(type(data))

# Converting to long
data1 = int(data, 16)
print(type(data1))
