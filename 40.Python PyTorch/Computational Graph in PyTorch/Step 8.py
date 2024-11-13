# define labels
labels = torch.rand(1).to(device)

# forward propagation
prediction = net(img)

# define loss
loss = (prediction - labels).sum()

# backward pass
loss.backward()
# Optimizer
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# gradient descent
optimizer.step()

# Computational Graph
make_dot(prediction,
		params=dict(net.named_parameters()))
