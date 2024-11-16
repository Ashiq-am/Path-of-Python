import numpy as np

prog_langs = ['python', 'c++', 'java', 'ruby']

# generating random samples
print(np.random.choice(prog_langs, size=(4, 5)))

# generating random samples with probabilities
print('\n')
print(np.random.choice(prog_langs, size=(10, 2),
					replace=True, p=[0.3, 0.5, 0.0, 0.2]))
