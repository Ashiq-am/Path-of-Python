for name, param in model.named_parameters():
    print(f"Parameter Name: {name}, Parameter Shape: {param.shape}")
