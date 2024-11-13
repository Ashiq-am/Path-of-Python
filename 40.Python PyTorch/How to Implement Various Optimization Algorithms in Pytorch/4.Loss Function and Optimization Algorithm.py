criterion = torch.nn.CrossEntropyLoss()

# SGD optimizer
optimizer_sgd = torch.optim.SGD(net.parameters(), lr=0.01, momentum=0.9)

# Adam optimizer
optimizer_adam = torch.optim.Adam(net.parameters(), lr=0.01, betas=(0.9, 0.999))

# Adagrad optimizer
optimizer_adagrad = torch.optim.Adagrad(net.parameters(), lr=0.01)

# Adadelta optimizer
optimizer_adadelta = torch.optim.Adadelta(net.parameters(), rho=0.9)
