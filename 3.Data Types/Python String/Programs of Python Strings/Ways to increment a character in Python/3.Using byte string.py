# python code to demonstrate way to
# increment character

# initializing byte character
ch = 'M'

# converting charater to byte
ch = bytes(ch, 'utf-8')

# adding 10 to M
s = bytes([ch[0] + 10])

# converting byte to string
s = str(s)

# printing the required value
print ("The value of M after incrementing 10 places is : ",end="")
print (s[2])
