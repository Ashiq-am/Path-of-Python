# generating the random tensor
# matrix of 4X4
rates_torch = torch.rand(4, 4) * 10
print(rates_torch)

# this function will do the poisson
# distribution od the given tensor
# and will give new tensor
# poisson(param),this param is the
# tensor matrix of 4X4
torch.poisson(rates_torch)
