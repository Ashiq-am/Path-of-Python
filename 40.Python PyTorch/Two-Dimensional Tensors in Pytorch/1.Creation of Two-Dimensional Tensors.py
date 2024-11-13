# importing library
import torch

# list of data in 1d form
y=torch.tensor([2.5,5.6,8.1,4.6,3.2,6.7])

# reshaping it to 2d
x=y.view(2,3)
print('First tensor is: {}'.format(x),'\nSize of it:{}'.format(x.size()),
	'\ntype of tensor:{}\n'.format(x.dtype))

# random values of size 2X2
x2=torch.randn(2,2)
print('Second tensor is: {}'.format(x2),'\nSize of it:{}'.format(x2.size()),
	'\ntype of tensor:{}\n'.format(x2.dtype))

# integers within this range
y1=torch.arange(0,8)
x1=y1.view(4,2)
print('Third tensor is: {}'.format(x1),'\nSize of it:{}'.format(x1.size()),
	'\ntype of tensor:{}'.format(x1.dtype))
