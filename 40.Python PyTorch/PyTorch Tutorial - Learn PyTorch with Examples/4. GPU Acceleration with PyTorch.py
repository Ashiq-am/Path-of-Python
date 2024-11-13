import torch

# Step 1: Check if CUDA is available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')

# Step 2: Create a sample tensor and move it to the GPU
tensor_size = (10000, 10000)  # Size of the tensor
a = torch.randn(tensor_size, device=device)  # Random tensor on GPU
b = torch.randn(tensor_size, device=device)  # Another random tensor on GPU

# Step 3: Perform operations on GPU
c = a + b  # Element-wise addition

# Print the result (moving back to CPU for printing)
print("Result shape (moved to CPU for printing):", c.cpu().shape)

# Optional: Check if GPU memory is being utilized
print("Current GPU memory usage:")
print(f"Allocated: {torch.cuda.memory_allocated(device) / (1024 ** 2):.2f} MB")
print(f"Cached: {torch.cuda.memory_reserved(device) / (1024 ** 2):.2f} MB")
