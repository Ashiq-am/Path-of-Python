d_input = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
res = {}
for i, v in d_input.items():
	res[v] = [i] if v not in res.keys() else res[v] + [i]
print(res)
