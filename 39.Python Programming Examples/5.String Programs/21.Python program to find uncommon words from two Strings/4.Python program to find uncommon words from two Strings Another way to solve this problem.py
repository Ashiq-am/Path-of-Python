def uncommon(A, B):
	un_comm = [i for i in "".join(B).split() if i not in "".join(A).split()]
	return un_comm

#Driver code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
print(uncommon(A, B))
