def REVERSE(L):
	L.reverse()
	return(L)
def YKNJS(L):
	List = []
	List.extend(REVERSE(L))
	print(List)

L = [1, 3.1, 5.31, 7.531]
YKNJS(L)
