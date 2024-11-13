class ModifiedResNet(nn.Module):
    def __init__(self):
        super(ModifiedResNet, self).__init__()
        self.resnet = torch.hub.load('pytorch/vision', 'resnet50', pretrained=True)
        num_classes = 10  # MNIST has 10 classes
        self.resnet.fc = nn.Linear(pretrained_model.fc.in_features, num_classes)  # Change the final fully connected layer for 10 classes

    def forward(self, x):
        return self.resnet(x)

model = ModifiedResNet()
