import torchvision.transforms as transforms
from PIL import Image

# Load an image (Make sure you have an example image)
image = Image.open('example.jpg')  # Replace 'example.jpg' with your image file

# Define a transformation: Random horizontal flip and convert to tensor
transform = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor()
])

# Apply the transformation to the image
augmented_image = transform(image)
print("Augmented Image Shape:", augmented_image.shape)
