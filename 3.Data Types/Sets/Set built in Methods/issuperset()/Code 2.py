# Python program to demonstrate working
# of issuperset().

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}

print("A.issuperset(B) : ", A.issuperset(B))

print("B.issuperset(A) : ", B.issuperset(A))

print("A.issuperset(C) : ", A.issuperset(C))

print("C.issuperset(B) : ", C.issuperset(B))
