# import modules
from numpy import isnan
from sklearn.impute import SimpleImputer
value = df.values

# defining the imputer
imputer = SimpleImputer(missing_values=nan,
						strategy='median')

# transform the dataset
transformed_values = imputer.fit_transform(value)

# count the number of NaN values in each column
print("Missing:", isnan(transformed_values).sum())
