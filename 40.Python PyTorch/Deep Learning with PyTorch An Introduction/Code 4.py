y = activation(torch.mm(features, weights.view(5, 1)) + bias)
