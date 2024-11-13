# Define problem domain
bounds = [(-5.0, 5.0) for _ in range(2)]  # for a 2-dimensional Rastrigin function
n_iterations = 1000
step_size = 0.1
temp = 10

# Perform the simulated annealing search
best, score, scores = simulated_annealing(objective_function, bounds, n_iterations, step_size, temp)

print(f'Best Solution: {best}')
print(f'Best Score: {score}')
