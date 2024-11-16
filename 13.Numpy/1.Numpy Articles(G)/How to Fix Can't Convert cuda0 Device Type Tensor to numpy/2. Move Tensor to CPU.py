import torch

# Create a tensor on GPU
gpu_tensor = torch.tensor([1, 2, 3], device='cuda')

# Move the tensor to CPU
cpu_tensor = gpu_tensor.cpu()

# Convert the CPU tensor to a NumPy array
numpy_array = cpu_tensor.numpy()

print(numpy_array)
