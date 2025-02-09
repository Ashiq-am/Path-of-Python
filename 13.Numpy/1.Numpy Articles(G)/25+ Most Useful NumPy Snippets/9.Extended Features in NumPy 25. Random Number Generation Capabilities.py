# Importing the random module
import numpy as np

# Generating random floats between 0 and 1
random_floats = np.random.rand(3, 2)
print("Random Floats:\n", random_floats)

# Generating random integers between a specified range
random_integers = np.random.randint(0, 10, size=(4,))
print("Random Integers:\n", random_integers)

# Generating samples from a normal distribution
normal_samples = np.random.normal(loc=0.0, scale=1.0, size=(5,))
print("Normal Distribution Samples:\n", normal_samples)