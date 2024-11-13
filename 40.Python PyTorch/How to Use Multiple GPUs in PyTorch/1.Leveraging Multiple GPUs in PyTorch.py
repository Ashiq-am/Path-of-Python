import torch

if torch.cuda.is_available():
    print("GPUs are available!")
else:
    print("No GPUs found.")
