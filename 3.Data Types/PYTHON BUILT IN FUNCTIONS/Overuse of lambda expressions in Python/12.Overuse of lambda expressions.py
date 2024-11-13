details = [{'p':100, 'r':0.01, 'n':2, 't':4},
		{'p':150, 'r':0.04, 'n':1, 't':5},
		{'p':120, 'r':0.05, 'n':5, 't':2}]
def CI(det):
	'''sort key: coumpound interest, P(1 + r/n)^(nt)'''
	return det['p']*((1 + det['r']/det['n'])**(det['n']*det['t']))
sorted_details = sorted(details, key=CI)
print(sorted_details)
