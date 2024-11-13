def EliasGammaEncode(k):
	if (k == 0):
		return '0'
	N = 1 + floor(log(k, 2))
	Unary = (N-1)*'0'+'1'
	return Unary + Binary_Representation_Without_MSB(k)
