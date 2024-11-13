le = preprocessing.LabelEncoder()

# Converting string labels of
# the 'species' column into numbers.
iris.species = le.fit_transform(iris.species)
print(iris.head())
