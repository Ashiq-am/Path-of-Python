# import torch
import torch

'''
Solve the linear equation - 9x - y = 0,
3x - 4y = 0 and check the solution is true or not

Here the elements of M is - [[9,-1],[3,-4]] and t - [0,0].
'''

# consider M which is an 2 D tensor that
# has 2 elements each
M = torch.tensor([[9., -1.], [3., -4.]])

# consider t which is an 1 D tensor that
# has 2 elements
t = torch.tensor([0., 0.])

# Solve t using linalg.solve(M,t) method
solved = torch.linalg.solve(M, t)

# display the solved solution
print(solved)

# check the solution is true or not using
# allclose() method
print(torch.allclose(M @ solved, t))
