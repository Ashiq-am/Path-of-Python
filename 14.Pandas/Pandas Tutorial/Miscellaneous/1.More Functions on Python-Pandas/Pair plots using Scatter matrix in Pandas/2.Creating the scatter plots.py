import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# selecting three numerical features
features = ['median_house_value', 'housing_median_age',
			'median_income']

# plotting the scatter matrix
# with the features
scatter_matrix(data[features])
plt.show()
