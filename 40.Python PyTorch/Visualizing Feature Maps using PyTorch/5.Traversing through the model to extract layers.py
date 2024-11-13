# Traverse through the model to extract convolutional layers and their weights
for module in pretrained_model.features.children():
	if isinstance(module, nn.Conv2d):
		total_conv_layers += 1
		conv_weights.append(module.weight)
		conv_layers.append(module)

print(f"Total convolution layers: {total_conv_layers}")
