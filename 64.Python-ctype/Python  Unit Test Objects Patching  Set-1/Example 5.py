x = 42
with patch('__main__.x'):
	print(x)

print (x)
