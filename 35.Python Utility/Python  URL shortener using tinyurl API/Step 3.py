def main():
	for tinyurl in map(make_tiny, sys.argv[1:]):
		print(tinyurl)

if __name__ == '__main__':
	main()


