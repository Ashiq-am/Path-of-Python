import os
import torch
import torch.distributed as dist
import torch.multiprocessing as mp
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.parallel import DistributedDataParallel as DDP


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 100)
        self.fc2 = nn.Linear(100, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


def init_process(rank, size, backend='gloo'):
    """ Initialize the distributed environment. """
    dist.init_process_group(backend, rank=rank, world_size=size)


def train(rank, size):
    # Set environment variables for distributed setup
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'

    # Initialize the process group
    init_process(rank, size)

    # Create the model and wrap it in DDP
    model = SimpleModel()
    model = DDP(model)

    # Define optimizer and loss function
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    loss_fn = nn.MSELoss()

    # Training loop
    for epoch in range(10):
        # Generate fake data for demonstration
        inputs = torch.randn(20, 10)
        targets = torch.randn(20, 1)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, targets)
        loss.backward()
        optimizer.step()

        if rank == 0:  # Print loss from the main process
            print(f'Epoch {epoch}, Loss: {loss.item()}')


def main():
    size = 2  # Number of processes
    mp.spawn(train, args=(size,), nprocs=size, join=True)


if __name__ == "__main__":
    main()
