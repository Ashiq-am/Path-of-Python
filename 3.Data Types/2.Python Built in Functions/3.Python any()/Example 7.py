# this function gives same result as built-in any() function
def my_any(list_x):
	for item in list_x:
		if item:
			return True
	return False

x = [4, 5, 8, 9, 10, 17]
print(my_any(x))
