import torch

# Create a tensor on GPU
gpu_tensor = torch.tensor([1, 2, 3], device='cuda')

# Convert the GPU tensor to a NumPy array in one step
numpy_array = gpu_tensor.cpu().numpy()

print(numpy_array)
