lst = [1, 2, 3]

ans = []

for x in lst:
	def res(x): return x*2
	ans.append(res(x))

print(ans)
