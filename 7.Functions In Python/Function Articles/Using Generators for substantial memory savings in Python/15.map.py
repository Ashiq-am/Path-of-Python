def map_func():
	m = map(lambda x, y: max([x, y]), [8, 2, 9], [5, 3, 7])
	return m

def main():
	m = map_func()
	print(next(m)) # 8 (maximum value among 8 and 5)
	print(next(m)) # 3 (maximum value among 2 and 3)
	print(next(m)) # 9 (maximum value among 9 and 7)

if __name__ == "__main__":
	main()
