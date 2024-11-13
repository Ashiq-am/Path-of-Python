def EliasDeltaEncode(x):
	Gamma = EliasGammaEncode(1 + floor(log(k, 2)))
	binary_without_MSB = Binary_Representation_Without_MSB(k)
	return Gamma+binary_without_MSB


k = int(input('Enter a number to encode in Elias Delta: '))
print(EliasDeltaEncode(k))
