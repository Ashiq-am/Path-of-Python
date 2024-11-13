def dict_func():
	dictionary = {'UserName': 'abc', 'Password':'a@123'}
	return dictionary

def main():
	d = dict_func()
	iterator = iter(d.items())
	print(next(iterator))
	print(next(iterator))

if __name__ == "__main__":
	main()
