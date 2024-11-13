from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

# First call to the function will execute the computation and cache the result
start_time = time.time()

result = fibonacci(10)
print(result)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

# Subsequent calls to the function with the same input will return the cached result
result = fibonacci(10)
print(result)
print("--- %s seconds ---" % (time.time() - start_time))
