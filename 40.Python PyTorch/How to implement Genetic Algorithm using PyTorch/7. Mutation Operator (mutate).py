# Mutation operator: Random mutation
def mutate(model):
    for param in model.parameters():
        if torch.rand(1).item() < mutation_rate:
            param.data += torch.randn_like(param.data) * 0.1  # Adding Gaussian noise with std=0.1
    return model