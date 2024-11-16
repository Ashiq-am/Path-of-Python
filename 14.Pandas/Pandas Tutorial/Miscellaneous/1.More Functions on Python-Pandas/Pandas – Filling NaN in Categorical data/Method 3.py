# using sklearn-pandas package
from sklearn_pandas import CategoricalImputer

# handling NaN values
imputer = CategoricalImputer()
data = np.array(df['Color'], dtype=object)
imputer.fit_transform(data)
