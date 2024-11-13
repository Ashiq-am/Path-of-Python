epochs = 10
prec = math.ceil(math.log10(epochs / 100))


model = VAE_gumbel(latent_dim)
model.to(device)

optimizer = optim.Adam(model.parameters(), lr=1e-3)
from torch.autograd import Variable

for epoch in range(1, epochs + 1):
	train(epoch, model, train_loader, optimizer, temp, True)
	test(epoch, model, test_loader, temp, True)
