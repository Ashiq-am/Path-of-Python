import torch

# Create a tensor on the GPU
gpu_tensor = torch.tensor([4.0, 5.0, 6.0], device='cuda:0')

# Move the tensor to the CPU
cpu_tensor = gpu_tensor.cpu()

# Convert the CPU tensor to a NumPy array
numpy_array = cpu_tensor.numpy()

print("GPU Tensor:", gpu_tensor)
print("CPU Tensor:", cpu_tensor)
print("NumPy Array:", numpy_array)
