# Main function
if __name__ == '__main__':
    # Set the number of processes and define the input and output data

    X = torch.tensor([[1], [2], [3], [4]], dtype=torch.float32)
    Y = torch.tensor([[2], [4], [6], [8]], dtype=torch.float32)
    n_samples, n_features = X.shape

    # Print the number of samples and features
    print(f'#samples: {n_samples}, #features: {n_features}')

    # Define the test input and the model input/output sizes
    X_test = torch.tensor([5], dtype=torch.float32)
    input_size = n_features
    output_size = n_features

    # Define the linear model and print its prediction on the test input before training
    model = nn.Linear(input_size, output_size)
    print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')

    # Number of processes
    num_processes = 4
    # Share the model's memory to allow it to be accessed by multiple processes
    model.share_memory()

    # Create a list of processes and start each process with the train function
    processes = []
    for rank in range(num_processes):
        p = mp.Process(target=train, args=(model, X, Y,), name=f'Process-{rank}')
        p.start()
        processes.append(p)
        print(f'Started {p.name}')

    # Wait for all processes to finish
    for p in processes:
        p.join()
        print(f'Finished {p.name}')

    # Print the model's prediction on the test input after training
    print(f'Prediction after training: f(5) = {model(X_test).item():.3f}')
