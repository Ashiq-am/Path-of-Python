from torch.utils.data import DataLoader, random_split

# Hyperparameters
sequence_length = 10
batch_size = 64
learning_rate = 0.001
num_epochs = 10

# Create the dataset
dataset = TextDataset(sequence_length)

# Split the dataset into training and validation sets
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = random_split(dataset,
								[train_size, val_size])

# Create data loaders
train_loader = DataLoader(train_dataset,
					batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset,
						batch_size=batch_size)

# Create the model
model = LSTMModel(dataset)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),\
							lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
	model.train()
	total_loss = 0.0

	for batch in train_loader:
		inputs, targets = batch

		optimizer.zero_grad()

		hidden = model.init_state(sequence_length)
		outputs, _ = model(inputs, hidden)

		loss = criterion(outputs.view(-1,
					len(dataset.unique_words)), \
						targets.view(-1))
		loss.backward()

		optimizer.step()

		total_loss += loss.item()

	# Calculate average loss for the epoch
	average_loss = total_loss / len(train_loader)

	# Print the epoch and average loss
	print(f"Epoch [{epoch+1}/{num_epochs}], Average Loss: {average_loss:.4f}")

	# Validation loop
	model.eval()
	val_loss = 0.0

	with torch.no_grad():
		for batch in val_loader:
			inputs, targets = batch

			hidden = model.init_state(sequence_length)
			outputs, _ = model(inputs, hidden)

			loss = criterion(outputs.view(-1,
							len(dataset.unique_words)), \
							targets.view(-1))
			val_loss += loss.item()

	# Calculate average validation loss for the epoch
	average_val_loss = val_loss / len(val_loader)

	# Print the epoch and average validation loss
	print(f"Epoch[{epoch+1}/{num_epochs}], Validation Loss: {average_val_loss: .4f}")
