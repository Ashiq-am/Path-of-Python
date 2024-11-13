import torchvision.transforms as transforms

# Define transformations
transform = transforms.Compose([
	transforms.Resize(256),			 # Resize images to 256x256
	transforms.RandomCrop(224),		 # Randomly crop images to 224x224
	transforms.RandomHorizontalFlip(), # Randomly flip images horizontally
	transforms.ToTensor(),			 # Convert images to PyTorch tensors
	transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
						0.229, 0.224, 0.225]) # Normalize images
])

# Example of applying transformations to image
example_image = transforms.ToPILImage()(
	torch.randn(3, 256, 256)) # Example image tensor
transformed_image = transform(example_image)


print("Transformed image shape:", transformed_image.shape)
