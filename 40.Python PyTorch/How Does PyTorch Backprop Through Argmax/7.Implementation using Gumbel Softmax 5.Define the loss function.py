latent_dim = 20
categorical_dim = 10 # one-of-K vector

temp = 1
temp_min = 0.5
ANNEAL_RATE = 0.00003

model = VAE_gumbel(temp).to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-3)


# Reconstruction + KL divergence losses summed over all elements and batch
def loss_function(recon_x, x, qy):
	BCE = F.binary_cross_entropy(recon_x, x.view(-1, 784), size_average=False) / x.shape[0]

	log_ratio = torch.log(qy * categorical_dim + 1e-20)
	KLD = torch.sum(qy * log_ratio, dim=-1).mean()

	return BCE + KLD
