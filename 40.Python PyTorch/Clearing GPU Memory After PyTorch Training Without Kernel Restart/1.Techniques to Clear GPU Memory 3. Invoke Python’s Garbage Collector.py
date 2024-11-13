import gc
import torch

# Simulate some memory usage by creating a large tensor
large_tensor = torch.randn(10000, 10000, device='cuda')
print(f"Memory allocated before clearing cache: {torch.cuda.memory_allocated()} bytes")

# Manually invoke garbage collection
gc.collect()

# Clear GPU cache
torch.cuda.empty_cache()
print(f"Memory allocated after clearing cache: {torch.cuda.memory_allocated()} bytes")
