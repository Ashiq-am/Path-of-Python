model = CustomNetwork()

from torchsummary import summary
summary(model, (1, 28, 28))
dummy_input = torch.randn(1, 1, 28, 28)
