transform = transforms.Compose([transforms.ToTensor(),
								transforms.Normalize((0.5,), (0.5,))])

trainset = torchvision.datasets.MNIST(root='./data', train=True,
										download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64,
										shuffle=True, num_workers=2)
