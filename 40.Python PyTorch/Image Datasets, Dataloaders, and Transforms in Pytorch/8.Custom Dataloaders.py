# Defining a custom data loader
dataloader = torch.utils.data.DataLoader(
    # Replace with the dataset object
    dataset=dataset,

    # Defining the batch size
    batch_size=4,

    # If true, shuffles the dataset at every epoch
    shuffle=True,

    # Number of parallel processes for loading the data
    num_workers=2
)

# Get the length of the dataloader
# (Number of batches)
print('Number of batches:', len(dataloader))
