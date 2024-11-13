# Creating a custom dataset class
class ImageDataset(torch.utils.data.Dataset):
    def __init__(self, dir, transform=None):
        self.data_dir = dir
        self.images = os.listdir(dir)
        self.transform = transform

    # Defining the length of the dataset
    def __len__(self):
        return len(self.images)

    # Defining the method to get an item from the dataset
    def __getitem__(self, index):
        image_path = os.path.join(self.data_dir, self.images[index])
        image = np.array(Image.open(image_path))

        # Applying the transform
        if self.transform:
            image = self.transform(image)

        return image
