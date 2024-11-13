def simulated_annealing(objective, bounds, n_iterations, step_size, temp):
    # Initial solution
    best = [random.uniform(bound[0], bound[1]) for bound in bounds]
    best_eval = objective(best)
    current, current_eval = best, best_eval
    scores = [best_eval]

    for i in range(n_iterations):
        # Decrease temperature
        t = temp / float(i + 1)
        # Generate candidate solution
        candidate = get_neighbor(current, step_size)
        candidate_eval = objective(candidate)
        # Check if we should keep the new solution
        if candidate_eval < best_eval or random.random() < math.exp((current_eval - candidate_eval) / t):
            current, current_eval = candidate, candidate_eval
            if candidate_eval < best_eval:
                best, best_eval = candidate, candidate_eval
                scores.append(best_eval)

        # Optional: print progress
        if i % 100 == 0:
            print(f"Iteration {i}, Temperature {t:.3f}, Best Evaluation {best_eval:.5f}")

    return best, best_eval, scores
