# Crossover operator: Single-point crossover
def crossover(parent1, parent2):
    child1 = CNN()
    child2 = CNN()
    child1.conv1.weight.data = torch.cat((parent1.conv1.weight.data[:16], parent2.conv1.weight.data[16:]), dim=0)
    child2.conv1.weight.data = torch.cat((parent2.conv1.weight.data[:16], parent1.conv1.weight.data[16:]), dim=0)
    return child1, child2