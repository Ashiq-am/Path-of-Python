import sys
L1 = tuple()
print(sys.getsizeof(L1), end = " ")
L1 = (1, 2)
print(sys.getsizeof(L1), end = " ")
L1 = (1, 3, (4, 5))
print(sys.getsizeof(L1), end = " ")
L1 = (1, 2, 3, 4, 5, [3, 4], 'p', '8', 9.777, (1, 3))
print(sys.getsizeof(L1))
