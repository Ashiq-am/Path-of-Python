A = {1,2,3,4,6}
B = {1,2,5,8,9}
# Intersaction and Union of two sets can also be done using & and | operators.
C = A.intersection(B)
D = A.union(B)
print('AnB = ', C)
print('AUB = ', D)
print('J(A,B) = ', float(len(C))/float(len(D)))
