s = "banana"
s_list = list(s)
 # Modify the second character
s_list[1] = 'A'
 # Convert back to string
s = ''.join(s_list)
print(s)