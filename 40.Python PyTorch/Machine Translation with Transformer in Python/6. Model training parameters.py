# Access the layers and freeze the specified number of layers
# Specify the number of layers to freeze from the end

for parameter in model.parameters():
	parameter.requires_grad = True
num_layers_to_freeze = 10 # Adjust as needed
for layer_index, layer in enumerate(model.model.encoder.layers):
	print
	if layer_index < len(model.model.encoder.layers) - num_layers_to_freeze:
		for parameter in layer.parameters():
			parameter.requires_grad = False

num_layers_to_freeze = 10 # Adjust as needed
for layer_index, layer in enumerate(model.model.decoder.layers):
	print
	if layer_index < len(model.model.encoder.layers) - num_layers_to_freeze:
		for parameter in layer.parameters():
			parameter.requires_grad = False
