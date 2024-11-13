class VAE_gumbel(nn.Module):
	def __init__(self, temp):
		super(VAE_gumbel, self).__init__()

		self.fc1 = nn.Linear(784, 512)
		self.fc2 = nn.Linear(512, 256)
		self.fc3 = nn.Linear(256, latent_dim * categorical_dim)

		self.fc4 = nn.Linear(latent_dim * categorical_dim, 256)
		self.fc5 = nn.Linear(256, 512)
		self.fc6 = nn.Linear(512, 784)

		self.relu = nn.ReLU()
		self.sigmoid = nn.Sigmoid()

	def encode(self, x):
		h1 = self.relu(self.fc1(x))
		h2 = self.relu(self.fc2(h1))
		return self.relu(self.fc3(h2))

	def decode(self, z):
		h4 = self.relu(self.fc4(z))
		h5 = self.relu(self.fc5(h4))
		return self.sigmoid(self.fc6(h5))

	def forward(self, x, temp=0, hard=False):
		q = self.encode(x.view(-1, 784))
		q_y = q.view(q.size(0), latent_dim, categorical_dim)
		z = gumbel_softmax(q_y, temp, hard)
		return self.decode(z), F.softmax(q_y, dim=-1).reshape(*q.size())
