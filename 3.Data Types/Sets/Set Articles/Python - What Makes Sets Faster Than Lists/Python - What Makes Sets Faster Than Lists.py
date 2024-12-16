import timeit

# Create a list and set with 10,000 elements
a = range(10000)
s = set(a)

# Measure membership test times
t1= timeit.timeit(lambda: 9999 in a, number=1000)
t2 = timeit.timeit(lambda: 9999 in s, number=1000)

print(f"List time: {t1:.6f} | Set time: {t2:.6f}")