from math import sqrt
L1 = [x**2 for x in range(10)].pop()
L1 += 19
print(sqrt(L1), end = " ")
L1 = [x**2 for x in reversed(range(10))].pop()
L1 += 16
print(int(sqrt(L1)))
