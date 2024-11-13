class CustomResNet(nn.Module):
    def __init__(self, pretrained_model):
        super(CustomResNet, self).__init__()
        self.resnet = torch.hub.load('pytorch/vision', 'resnet50', pretrained=True)
        self.features = nn.Sequential(*list(pretrained_model.children())[:-1])
        self.classifier = nn.Linear(pretrained_model.fc.in_features, 10)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

model = CustomResNet(pretrained_model)
