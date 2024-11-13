# import the torch and
# torchvision dataset packages.
import torch
import torchvision

# access the dataset in torchvision package using
# .datasets followed by dataset name.
imagenet_data = torchvision.datasets.ImageNet('path/to/imagenet_root/')
