num_epochs = 2

for epoch in range(num_epochs):
	for i, (inputs, labels) in enumerate(dataloader):

		# here: 303 samples, batch_size = 4, n_iters=303/4=75 iterations
		# Run our training process
		if (i+1) % 5 == 0:
			print(f'Epoch: {epoch+1}/{num_epochs}, Step {i+1}/{n_iterations}|\
				Inputs {inputs.shape} | Labels {labels.shape}')
