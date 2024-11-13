# Check CUDA availability
if not torch.cuda.is_available():
    raise RuntimeError("No CUDA available, please use a GPU runtime.")
