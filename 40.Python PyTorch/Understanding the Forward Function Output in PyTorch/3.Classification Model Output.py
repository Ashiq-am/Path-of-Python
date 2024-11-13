class ClassificationModel(nn.Module):
    def __init__(self):
        super(ClassificationModel, self).__init__()
        self.linear = nn.Linear(10, 3)  # Output 3 class scores

    def forward(self, x):
        return self.linear(x)


model = ClassificationModel()
input_data = torch.randn(1, 10)
logits = model(input_data)
print(logits)  # Raw logits for 3 classes
