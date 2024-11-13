L = [2e-04, 'a', False, 87]
T = (6.22, 'boy', True, 554)
for i in range(len(L)):
	if L[i]:
		L[i] = L[i] + T[i]
	else:
		T[i] = L[i] + T[i]
		break
