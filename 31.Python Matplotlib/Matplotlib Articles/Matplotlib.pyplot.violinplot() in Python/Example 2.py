import matplotlib.pyplot as plt

# Fixing random state for
# reproducibility
from plotly.figure_factory import np

np.random.seed(15437660)

# creating randomly generate
# collections / data
coll_1 = np.random.normal(100, 10, 200)
coll_2 = np.random.normal(80, 30, 200)
coll_3 = np.random.normal(90, 20, 200)
coll_4 = np.random.normal(70, 25, 200)

## combining these different
# collections into a list
data_plotter = [coll_1, coll_2,
				coll_3, coll_4]

plt.violinplot(data_plotter)

plt.show()
