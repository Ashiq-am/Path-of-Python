import torch
from torch import nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torch.optim import SGD
from torch.optim.lr_scheduler import ReduceLROnPlateau
from tqdm.notebook import trange

# LOADING DATA
transform = transforms.Compose([
    transforms.ToTensor()
])

train = datasets.MNIST('', train=True, download=True, transform=transform)
valid = datasets.MNIST('', train=False, download=True, transform=transform)

trainloader = DataLoader(train, batch_size=32, shuffle=True)
validloader = DataLoader(test, batch_size=32, shuffle=True)


# CREATING OUR MODEL
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 64)
        self.fc2 = nn.Linear(64, 32)
        self.out = nn.Linear(32, 10)
        self.lr = 0.01
        self.loss = nn.CrossEntropyLoss()

    def forward(self, x):
        batch_size, _, _, _ = x.size()
        x = x.view(batch_size, -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.out(x)


model = Net()

# Send the model to GPU if available
if torch.cuda.is_available():
    model = model.cuda()

# SETTING OPTIMIZER, LOSS AND SCHEDULER
optimizer = SGD(model.parameters(), lr=0.1)
loss = nn.CrossEntropyLoss()
scheduler = ReduceLROnPlateau(optimizer, 'min', patience=5)

# TRAINING THE NEURAL NETWORK
epoch = 25
for e in trange(epoch):
    train_loss, valid_loss = 0.0, 0.0

    # Set model to training mode
    model.train()
    for data, label in trainloader:
        if torch.cuda.is_available():
            data, label = data.cuda(), label.cuda()

        optimizer.zero_grad()
        target = model(data)
        train_step_loss = loss(target, label)
        train_step_loss.backward()
        optimizer.step()

        train_loss += train_step_loss.item() * data.size(0)

    # Set model to Evaluation mode
    model.eval()
    for data, label in validloader:
        if torch.cuda.is_available():
            data, label = data.cuda(), label.cuda()

        target = model(data)
        valid_step_loss = loss(target, label)

        valid_loss += valid_step_loss.item() * data.size(0)

    curr_lr = optimizer.param_groups[0]['lr']

    print(f'Epoch {e}\t Training Loss: {train_loss / len(trainloader)}\t Validation Loss: {valid_loss / len(validloader)}\t LR: {curr_lr}')
    scheduler.step(valid_loss / len(validloader))
