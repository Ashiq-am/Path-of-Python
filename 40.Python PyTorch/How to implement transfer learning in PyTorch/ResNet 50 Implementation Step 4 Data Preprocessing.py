from torchvision.transforms.functional import pad

transform_train = transforms.Compose([
    transforms.RandomRotation(10),
    transforms.Grayscale(num_output_channels=3),  # Convert to RGB format
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])  # Normalize as before
])

transform_test = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),  # Convert to RGB format
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5], std=[0.5])
])
