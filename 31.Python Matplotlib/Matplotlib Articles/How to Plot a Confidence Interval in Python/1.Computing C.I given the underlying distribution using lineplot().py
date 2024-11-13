# import libraries
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# generate random data
np.random.seed(0)
x = np.random.randint(0, 30, 100)
y = x+np.random.normal(0, 1, 100)

# create lineplot
ax = sns.lineplot(x, y)
