# Load and modify the model
num_classes= 10                     #Class size of MNIST dataset
model = models.vgg16(pretrained=True)
num_features = model.classifier[6].in_features
model.classifier[6] = nn.Linear(num_features, num_classes)
