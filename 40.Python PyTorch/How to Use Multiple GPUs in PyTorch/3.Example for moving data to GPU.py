# Example for moving data to GPU
input_data = torch.randn(64, 1024).to('cuda')
output = model(input_data)
