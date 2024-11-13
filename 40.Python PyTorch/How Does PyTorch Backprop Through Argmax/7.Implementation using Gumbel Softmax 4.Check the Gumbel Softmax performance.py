temp=1
latent_dim = 2
categorical_dim=5
input = torch.rand(1,latent_dim*categorical_dim)
print('Input:', input)
# With hard = False
print('\nGumbel Softmax with hard=False\n',gumbel_softmax(input, temp,False))
#With hard = True
print('\nGumbel Softmax with hard=True\n',gumbel_softmax(input, temp, True))
