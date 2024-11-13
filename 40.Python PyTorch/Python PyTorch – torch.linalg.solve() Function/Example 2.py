# import torch
import torch

'''
Let's consider the linear equations :
5x - 3y = 0
3x - 4y = 2
Then M values can be - [[5,-3],[3,-4]]
and t is [0,2]
'''

# consider M which is an 2 D tensor that
# has 2 elements each
M = torch.tensor([[5., -3.], [3., -4.]])

# consider t which is an 1 D tensor that
# has 2 elements
t = torch.tensor([0., 2.])

# Solve the equation using linalg.solve(M,t)
# method
solved = torch.linalg.solve(M, t)

# display the solved solution
print(solved)

# check the solution is true or not using
# allclose() method
print(torch.allclose(M @ solved, t))
