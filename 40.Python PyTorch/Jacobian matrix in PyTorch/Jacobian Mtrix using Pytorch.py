from torch.autograd.functional import jacobian
from torch import tensor

#Defining the main function
def f(x1,x2,x3):
	return (x1 + x2, x3*x1, x2**3)

#Defining input tensors
x1 = tensor(3.0)
x2 = tensor(4.0)
x3 = tensor(5.0)

#Printing the Jacobian
print(jacobian(f,(x1,x2,x3)))
