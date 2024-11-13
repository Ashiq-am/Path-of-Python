# single dimensional matrices
oneD_1 = torch.tensor([3, 6, 2])
oneD_2 = torch.tensor([4, 1, 9])


# two dimensional matrices
twoD_1 = torch.tensor([[1, 2, 3],
					[4, 3, 8],
					[1, 7, 2]])
twoD_2 = torch.tensor([[2, 4, 1],
					[1, 3, 6],
					[2, 6, 5]])

# N-dimensional matrices (N>2)

# 2x3x3 dimensional matrix
ND_1 = torch.tensor([[[-0.0135, -0.9197, -0.3395],
					[-1.0369, -1.3242, 1.4799],
					[-0.0182, -1.2917, 0.6575]],

					[[-0.3585, -0.0478, 0.4674],
					[-0.6688, -0.9217, -1.2612],
					[1.6323, -0.0640, 0.4357]]])

# 2x3x4 dimensional matrix
ND_2 = torch.tensor([[[0.2431, -0.1044, -0.1437, -1.4982],
					[-1.4318, -0.2510, 1.6247, 0.5623],
					[1.5265, -0.8568, -2.1125, -0.9463]],

					[[0.0182, 0.5207, 1.2890, -1.3232],
					[-0.2275, -0.8006, -0.6909, -1.0108],
					[1.3881, -0.0327, -1.4890, -0.5550]]])

print("1D matrices output :\n", oneD_1 @ oneD_2)
print("\n2D matrices output :\n", twoD_1 @ twoD_2)
print("\nN-D matrices output :\n", ND_1 @ ND_2)
print("\n Mixed matrices output :\n", oneD_1 @ twoD_1 @ twoD_2)
