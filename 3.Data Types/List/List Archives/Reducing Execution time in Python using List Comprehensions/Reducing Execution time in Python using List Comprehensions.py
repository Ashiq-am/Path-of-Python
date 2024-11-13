import time

# Using for loop
start = time.time()
a = []

for i in range(10 ** 7):
    if i % 2 == 0:
        a.append(i)

print("Execution time = ", time.time() - start)

# Using list comprehension
start = time.time()

a = [i for i in range(10 ** 7) if i % 2 == 0]
print("Execution time = ", time.time() - start)
