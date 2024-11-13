# Sample dictionary
population = {'New York': 8398748, 'Los Angeles': 3980400, 'Chicago': 2716000, 'Houston': 2328000}

# Iterating and filtering elements based on population
for city, pop in enumerate((city, pop) for city, pop in population.items() if pop > 3000000):
	print(f"City: {city}, Population: {pop}")
