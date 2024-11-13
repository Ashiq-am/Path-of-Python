# Get the labels from the dataset
labels = [example.label for example in train_data.examples]

# Convert labels to numeric format
numeric_labels = [1 if label == 'positive' else 0 for label in labels]

# Print the numeric labels
print("Numeric Labels:", numeric_labels)
