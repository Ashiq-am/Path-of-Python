# this function have 2 parameters,
# and will form the tensor of
# normal distribution
# normal(mean,std)
# mean, giving a range of mean
# std,dive the standard in the given range
torch.normal(mean=torch.arange(12., 22.),
			std=torch.arange(1, 0, -0.1))
