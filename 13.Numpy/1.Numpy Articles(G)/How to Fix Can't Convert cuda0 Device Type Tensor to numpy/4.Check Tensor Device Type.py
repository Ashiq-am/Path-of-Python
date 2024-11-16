import torch

def to_numpy(tensor):
    if tensor.device.type == 'cuda':
        tensor = tensor.cpu()
    return tensor.numpy()

# Create a tensor on GPU
gpu_tensor = torch.tensor([1, 2, 3], device='cuda')

# Convert to NumPy array using the function
numpy_array = to_numpy(gpu_tensor)

print(numpy_array)
