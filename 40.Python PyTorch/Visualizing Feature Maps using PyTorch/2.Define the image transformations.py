# Define the image transformations
image_transform = transforms.Compose([
	transforms.Resize((224, 224)), # Resize the image to 224x224 pixels
	transforms.ToTensor(), # Convert the image to a PyTorch tensor
	transforms.Normalize(mean=0., std=1.) # Normalize the image tensor
])
