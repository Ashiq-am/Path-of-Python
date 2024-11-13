# Initialize genetic algorithm parameters
def initialize_population():
    population = []
    for _ in range(population_size):
        model = CNN()
        population.append(model)
    return population