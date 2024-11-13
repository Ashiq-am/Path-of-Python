class MiniVGG(nn.Module):  # Smaller VGG for MNIST
  def __init__(self):
    super(MiniVGG, self).__init__()
    self.features = nn.Sequential(
      nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1),  # Input: 1 channel
      nn.ReLU(inplace=True),
      nn.MaxPool2d(kernel_size=2, stride=2),
      nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
      nn.ReLU(inplace=True),
      nn.MaxPool2d(kernel_size=2, stride=2),
      nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1),
      nn.ReLU(inplace=True),
      nn.MaxPool2d(kernel_size=2, stride=2)
    )
    self.avgpool = nn.AdaptiveAvgPool2d((7, 7))
    self.classifier = nn.Linear(64 * 7 * 7, 10)  # 10 output neurons for MNIST

  def forward(self, x):
    x = self.features(x)
    x = self.avgpool(x)
    x = x.view(x.size(0), -1)  # Flatten
    x = self.classifier(x)
    return x


model = MiniVGG()
