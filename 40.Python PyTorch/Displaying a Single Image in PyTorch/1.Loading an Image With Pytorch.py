from torchvision import transforms
from PIL import Image
import requests
from io import BytesIO

# URL of the image
image_url = 'https://picsum.photos/200/300'

# Download the image
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Define a transform to convert the image to a tensor
transform = transforms.Compose([
    transforms.ToTensor()
])

# Apply the transform to the image
image_tensor = transform(image)
