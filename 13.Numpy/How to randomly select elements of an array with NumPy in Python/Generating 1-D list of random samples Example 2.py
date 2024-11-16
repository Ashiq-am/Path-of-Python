import numpy as np

samples = 5
# generating random samples
print(np.random.choice(samples, size=10))

# generating random samples without replacement
print(np.random.choice(samples, size=5, replace=False))

# generating random samples with probablities
print(np.random.choice(samples, size=5, replace=True))

# generating with probabilities
print(np.random.choice(samples, size=15,
					replace=True, p=[0.2, 0.1, 0.1, 0.3, 0.3]))
