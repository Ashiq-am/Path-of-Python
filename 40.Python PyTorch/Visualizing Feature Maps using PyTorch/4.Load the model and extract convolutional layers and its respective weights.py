# Load a pre-trained VGG16 model
pretrained_model = models.vgg16(pretrained=True)

# Extract convolutional layers and their weights
conv_weights = [] # List to store convolutional layer weights
conv_layers = [] # List to store convolutional layers
total_conv_layers = 0 # Counter for total convolutional layers
