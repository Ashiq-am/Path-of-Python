# Move the model to GPU if available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
pretrained_model = pretrained_model.to(device)

# Preprocess the image and move it to GPU
input_image = image_transform(input_image)
input_image = input_image.unsqueeze(0) # Add a batch dimension
input_image = input_image.to(device)

# Extract feature maps
feature_maps = [] # List to store feature maps
layer_names = [] # List to store layer names
for layer in conv_layers:
	input_image = layer(input_image)
	feature_maps.append(input_image)
	layer_names.append(str(layer))
