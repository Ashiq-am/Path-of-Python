def fact(a):
	factors = []
	for i in range(1, a+1):
		if a%i == 0:
			factors.append(i)
	return factors

num = 600851475143
print(fact(num))
