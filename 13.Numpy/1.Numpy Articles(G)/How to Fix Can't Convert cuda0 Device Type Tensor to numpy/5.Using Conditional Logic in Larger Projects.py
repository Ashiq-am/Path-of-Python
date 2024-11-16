import torch

def tensor_to_numpy(tensor):
    if tensor.is_cuda:
        tensor = tensor.cpu()
    return tensor.numpy()

# Example usage with a tensor on GPU
gpu_tensor = torch.tensor([1, 2, 3], device='cuda')
numpy_array = tensor_to_numpy(gpu_tensor)
print(numpy_array)

# Example usage with a tensor on CPU
cpu_tensor = torch.tensor([4, 5, 6])
numpy_array = tensor_to_numpy(cpu_tensor)
print(numpy_array)
