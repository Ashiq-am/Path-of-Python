for name, module in model.named_modules():
    print(f"Layer Name: {name}, Layer Type: {type(module)}")
