# import the necessary libraries and functions
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor
import pytorch_lightning as pl


# Build the pytorch_lightning model
class Net(pl.LightningModule):
    def __init__(self):
        super(Net, self).__init__()
        self.layer1 = nn.Linear(28 * 28, 128)
        self.layer2 = nn.Linear(128, 10)
        self.out = nn.Linear(128, 10)
        self.lr = 0.01
        self.loss = nn.CrossEntropyLoss()

    def forward(self, x):
        x = x.view(-1, 28 * 28)
        x = nn.functional.relu(self.layer1(x))
        x = self.layer2(x)
        return nn.functional.log_softmax(x, dim=1)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = nn.functional.nll_loss(y_hat, y)
        logs = {'train_loss': loss}
        return {'loss': loss, 'log': logs}

    def configure_optimizers(self):
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

    def train_dataloader(self):
        return DataLoader(MNIST('data', train=True,
                                download=True,
                                transform=ToTensor()
                                ), batch_size=64)

    def test_dataloader(self):
        return DataLoader(MNIST('data',
                                train=False,
                                download=True,
                                transform=ToTensor()
                                ), batch_size=64)
    # Initialize the model


model = Net()
# Train themodel
trainer = pl.Trainer(accelerator='cuda', max_epochs=5)
trainer.fit(model)
