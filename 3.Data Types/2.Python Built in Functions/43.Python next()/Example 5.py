import time

# initializing list
l = [1, 2, 3, 4, 5]

# Creating iterator from list
l_iter = iter(l)

print("[Using next()]The contents of list are:")

# Iterating using next()
start_next = time.time_ns()
while (1):
	val = next(l_iter, 'end')
	if val == 'end':
		break
	else:
		print(val, end=" ")

print(f"\nTime taken when using next()\
is : {(time.time_ns() - start_next) / 10**6:.02f}ms")

# Iterating using for-loop
print("\n[Using For-Loop] The contents of list are:")
start_for = time.time_ns()
for i in l:
	print(i, end=" ")
print(f"\nTime taken when using for loop is\
: {(time.time_ns() - start_for) / 10**6:.02f}ms")
