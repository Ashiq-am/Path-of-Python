# Python code to demonstrate
# pad spaces in string
# upto fixed length

# initialising string
ini_string = "123abcjw"
padding_size = 15

# printing string and its length
print ("initial string : ", ini_string, len(ini_string))

# code to pad spaces in string
res = ini_string.ljust(padding_size)

# printing string and its length
print ("final string : ", res, len(res))
