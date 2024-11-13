# Python code to merge all sublist having common elements.

# Using recursion to merge all sublist having common elements.
def merge(Input, _start, _c = [], _seen = [], _used=[]):
	elem = [x for x in Input if any(y in _start for y in x)
	and x not in _seen and x not in _used]
	if not elem:
		yield set(_c)
		for x in Input:
			if x != _start and x not in _used:
				yield from merge(Input, x, _c=[], _seen=[],
						_used=_used+[x, *elem])
	else:
		yield from merge(Input, _start, _c = _c + [x for
											y in elem for x in y],
					_seen=_seen + elem, _used = _used + elem)

#Input list Initialization
Input = [[11, 27, 13], [11, 27, 55], [22, 0, 43],
		[22, 0, 96], [13, 27, 11], [13, 27, 55],
		[43, 0, 22], [43, 0, 96], [55, 27, 11]]

#Calling merge function
Output = list(map(list, {tuple(x) for
						x in merge(Input, Input[0], _seen=[Input[0]])
						if x}))

#Printing output
print("Initial list of list is :")
print(Input)
print("List of list after merging is:")
print(Output)
