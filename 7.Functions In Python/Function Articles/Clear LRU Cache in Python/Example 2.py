import functools

@functools.lru_cache(maxsize = None)
def fib(n):
	if n < 2:
		return n
	return fib(n-1) + fib(n-2)

fib(30)

# Before Clearing
print(fib.cache_info())

fib.cache_clear()

# After Clearing
print(fib.cache_info())
