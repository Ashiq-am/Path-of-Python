# Example usage:
csv_file = 'phishing_data.csv'
dataset = CustomDataset(csv_file)

# Create DataLoader
BATCH_SIZE = 64
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)