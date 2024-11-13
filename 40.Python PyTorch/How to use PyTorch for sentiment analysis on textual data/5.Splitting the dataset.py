padded_reviews_tensor = torch.tensor(padded_reviews, dtype=torch.long)
numeric_labels_tensor = torch.tensor(numeric_labels, dtype=torch.float)

# Check if sizes match and correct if needed
if padded_reviews_tensor.size(0) != numeric_labels_tensor.size(0):
    min_size = min(padded_reviews_tensor.size(0), numeric_labels_tensor.size(0))
    padded_reviews_tensor = padded_reviews_tensor[:min_size]
    numeric_labels_tensor = numeric_labels_tensor[:min_size]

# Combine features and labels into a TensorDataset
dataset = torch.utils.data.TensorDataset(padded_reviews_tensor, numeric_labels_tensor)

# Calculate the size of the training set
train_size = int(0.8 * len(dataset))
valid_size = len(dataset) - train_size

# Split the dataset into training and validation sets
train_data, valid_data = torch.utils.data.random_split(dataset, [train_size, valid_size])

# Extract features and labels for training and validation
X_train, y_train = zip(*train_data)
X_valid, y_valid = zip(*valid_data)

# Convert X_train, y_train, X_valid, y_valid to tensors (if needed)
X_train_tensor = torch.stack(X_train)
y_train_tensor = torch.stack(y_train)
X_valid_tensor = torch.stack(X_valid)
y_valid_tensor = torch.stack(y_valid)

# Print the shapes of the tensors (for verification)
print("X_train_tensor shape:", X_train_tensor.shape)
print("y_train_tensor shape:", y_train_tensor.shape)
print("X_valid_tensor shape:", X_valid_tensor.shape)
print("y_valid_tensor shape:", y_valid_tensor.shape)

# Print shapes of training and validation sets
print(f"Training Set - Features: {len(X_train)}, Labels: {len(y_train)}")
print(f"Validation Set - Features: {len(X_valid)}, Labels: {len(y_valid)}")
