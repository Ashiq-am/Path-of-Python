# Load the image
img = Image.open("Ganesh.jpg")

# Transformation
transform = transforms.Compose([
	transforms.Resize((720, 480)), # Resize the image to 720x480
	transforms.ToTensor(),
	transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

img = transform(img)
# Reshape the 4d tensor
img = img.view(1, 3, 720, 480)

# Move to GPU
img = img.to(device)
img.shape
