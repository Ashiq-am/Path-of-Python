# Define dataset class for loading and preprocessing images
class ImageDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.image_files = os.listdir(root_dir)

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.image_files[idx])
        image = Image.open(img_name).convert("RGB")
        if self.transform:
            image = self.transform(image)
        return image

# Define transforms (resize images for simplicity)
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Create Dataset and DataLoader
dataset = ImageDataset(root_dir="BSDS300/images/train", transform=transform)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)
