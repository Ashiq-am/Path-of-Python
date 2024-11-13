def range_func():
	r = range(0, 4)
	return r

def main():
	r = range_func()
	iterator = iter(r)
	print(next(iterator))
	print(next(iterator))

if __name__ == "__main__":
	main()
