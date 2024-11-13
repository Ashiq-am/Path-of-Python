import multiprocessing

def worker_function(arg):
	print(f"Worker process with arg: {arg}")

if __name__ == "__main__":
	with multiprocessing.Pool() as pool:
		result = pool.map(worker_function, range(5))
	pool.exit() # Incorrect usage causing AttributeError
