# import torch
import torch

'''
Let's consider the linear equations :
6x + 3y = 1
3x - 4y = 2
Then M values can be - [[6,3],[3,-4]]
and t is [1,2]
'''

# consider M which is an 2 D tensor that
# has 2 elements each
M = torch.tensor([[6., 3.], [3., -4.]])

# consider t which is 1D that has two elements
t = torch.tensor([1., 2.])

# Solve the equation using linalg.solve(M,t)
solved = torch.linalg.solve(M, t)

# display the solved solution
print(solved)

# check the solution is true or not using
# allclose() method
print(torch.allclose(M @ solved, t))
