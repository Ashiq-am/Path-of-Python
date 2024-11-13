# Our loss function
def my_loss(output, target):
	output = torch.tensor(output, dtype=torch.float)
	loss = ((output - target)**2).mean()
	return loss
# Our optimizer
optimizer = optim.SGD(model.parameters(),lr=0.001, momentum=0.9)
