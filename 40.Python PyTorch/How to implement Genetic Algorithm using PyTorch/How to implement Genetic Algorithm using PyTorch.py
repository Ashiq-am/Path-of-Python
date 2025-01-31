import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Define the neural network architecture (CNN)
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.max_pool2d(x, kernel_size=2, stride=2)
        x = torch.relu(self.conv2(x))
        x = torch.max_pool2d(x, kernel_size=2, stride=2)
        x = x.view(-1, 64 * 7 * 7)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return torch.log_softmax(x, dim=1)

# Function to compute fitness (accuracy) of an individual (hyperparameters)
def compute_fitness(model, train_loader, test_loader):
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.parameters())

    model.train()
    for epoch in range(5):
        for data, target in train_loader:
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            _, predicted = torch.max(output.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()

    accuracy = correct / total
    return accuracy

# Genetic algorithm parameters
population_size = 10
mutation_rate = 0.1
num_generations = 5

# Initialize genetic algorithm parameters
def initialize_population():
    population = []
    for _ in range(population_size):
        model = CNN()
        population.append(model)
    return population

# Crossover operator: Single-point crossover
def crossover(parent1, parent2):
    child1 = CNN()
    child2 = CNN()
    child1.conv1.weight.data = torch.cat((parent1.conv1.weight.data[:16], parent2.conv1.weight.data[16:]), dim=0)
    child2.conv1.weight.data = torch.cat((parent2.conv1.weight.data[:16], parent1.conv1.weight.data[16:]), dim=0)
    return child1, child2

# Mutation operator: Random mutation
def mutate(model):
    for param in model.parameters():
        if torch.rand(1).item() < mutation_rate:
            param.data += torch.randn_like(param.data) * 0.1  # Adding Gaussian noise with std=0.1
    return model

# Load MNIST dataset
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_dataset = datasets.MNIST(root='./data', train=True, transform=transform, download=True)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_dataset = datasets.MNIST(root='./data', train=False, transform=transform, download=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# Genetic algorithm
population = initialize_population()
for generation in range(num_generations):
    print("Generation:", generation + 1)
    best_accuracy = 0
    best_individual = None

    # Compute fitness for each individual
    for individual in population:
        fitness = compute_fitness(individual, train_loader, test_loader)
        if fitness > best_accuracy:
            best_accuracy = fitness
            best_individual = individual

    print("Best accuracy in generation", generation + 1, ":", best_accuracy)
    print("Best individual:", best_individual)

    next_generation = []

    # Select top individuals for next generation
    selected_individuals = population[:population_size // 2]

    # Crossover and mutation
    for i in range(0, len(selected_individuals), 2):
        parent1 = selected_individuals[i]
        parent2 = selected_individuals[i + 1]
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        next_generation.extend([child1, child2])

    population = next_generation

# Print final population
print("Final population:")
for individual in population:
    print("Individual:", individual)
