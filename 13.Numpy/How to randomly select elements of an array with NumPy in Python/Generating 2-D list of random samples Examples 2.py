import numpy as np

samples = 5

# generating random samples
print(np.random.choice(samples, size=(5, 5)))

# generating with probabilities
print('\n')
print(np.random.choice(samples, size=(8, 3),
					replace=True,
					p=[0.2, 0.1, 0.1, 0.3, 0.3]))
