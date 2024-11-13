def zip_func():
	z = zip(['a', 'b', 'c', 'd'], [1, 2, 3, 4])
	return z

def main():
	z = zip_func()
	print(next(z))
	print(next(z))
	print(next(z))

if __name__ == "__main__":
	main()
