import torch

a=torch.arange(0,9)

# reshaping data
a = mat_a.view(3,3)

b = torch.arange(0,9)

# reshaping data
b = mat_b.view(3,3)

mat_mul=torch.matmul(mat_a,mat_b)
elem_mul=torch.mul(mat_a,mat_b)
print('Tensor after elementwise multiplication:{}'.format(elem_mul),
	'\n Tensor after matrix multiplication: {}'.format(mat_mul))
