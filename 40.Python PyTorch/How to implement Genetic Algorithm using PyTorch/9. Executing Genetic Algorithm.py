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