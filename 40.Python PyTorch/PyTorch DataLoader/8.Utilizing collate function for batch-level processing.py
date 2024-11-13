from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence
import torch

class CustomDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]


def custom_collate(batch):
    # Separate the input features and labels
    inputs = [item[0] for item in batch]
    labels = [item[1] for item in batch]

    # Pad sequences to the same length (if input features are sequences)
    inputs_padded = pad_sequence(inputs, batch_first=True, padding_value=0)

    return inputs_padded, torch.tensor(labels)

# Example usage
data = [(torch.tensor([1, 2, 3]), 0),
        (torch.tensor([4, 5]), 1),
        (torch.tensor([6, 7, 8, 9]), 0)]


custom_dataset = CustomDataset(data)

data_loader = DataLoader(custom_dataset, batch_size=2, collate_fn=custom_collate)

# Iterate over batches
for batch_inputs, batch_labels in data_loader:
    print("Batch Inputs:", batch_inputs)
    print("Batch Labels:", batch_labels)
