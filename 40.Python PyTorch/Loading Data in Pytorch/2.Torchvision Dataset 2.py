# import necessary function
# from torchvision package
from torchvision import transforms, datasets
import matplotlib.pyplot as plt

# specify the image dataset folder
data_dir = r'path to dataset\train'

# perform some transformations like resizing,
# centring and tensorconversion
# using transforms function
transform = transforms.Compose(
	[transforms.Resize(255),
	transforms.CenterCrop(224),
	transforms.ToTensor()])

# pass the image data folder and
# transform function to the datasets
# .imagefolder function
dataset = datasets.ImageFolder(data_dir,
							transform=transform)

# now use dataloder function load the
# dataset in the specified transformation.
dataloader = torch.utils.data.DataLoader(dataset,
										batch_size=32,
										shuffle=True)

# iter function iterates through all the
# images and labels and stores in two variables
images, labels = next(iter(dataloader))

# print the total no of samples
print('Number of samples: ', len(images))
image = images[2][0] # load 3rd sample

# visualize the image
plt.imshow(image, cmap='gray')

# print the size of image
print("Image Size: ", image.size())

# print the label
print(label)
