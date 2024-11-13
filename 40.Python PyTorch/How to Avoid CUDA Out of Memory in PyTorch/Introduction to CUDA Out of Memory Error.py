import torch

# Check if CUDA is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available! Using GPU.")

    try:
        # Allocate a large tensor on the GPU (this size will likely exceed your GPU memory)
        large_tensor = torch.randn((100000, 10000, 10000), device=device)
        print("Tensor created successfully!")
    except RuntimeError as e:
        # Catch the CUDA Out of Memory error
        print(f"Caught a RuntimeError: {e}")
else:
    print("CUDA is not available. Please run this code on a system with a GPU.")
