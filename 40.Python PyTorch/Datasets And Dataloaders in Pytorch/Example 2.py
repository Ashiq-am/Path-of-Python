# Loading whole dataset with DataLoader
# shuffle the data, which is good for training
dataloader = DataLoader(dataset=dataset, batch_size=4, shuffle=True)

# total samples of data and number of iterations performed
total_samples = len(dataset)
n_iterations = total_samples//4
print(total_samples, n_iterations)
for i, (targets, labels) in enumerate(dataloader):
	print(targets, labels)
