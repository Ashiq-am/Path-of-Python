print("x : ", x)

with patch('__main__.x', 'patched_value'):
	print(x)
patched_value

print("x : ", x)
