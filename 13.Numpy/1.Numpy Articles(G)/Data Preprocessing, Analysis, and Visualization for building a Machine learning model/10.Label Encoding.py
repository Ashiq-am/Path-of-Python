le = LabelEncoder()
dataset['Geography'] = le.fit_transform(dataset["Geography"])
dataset['Gender'] = le.fit_transform(dataset["Gender"])
