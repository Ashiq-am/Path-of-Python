from sklearn.preprocessing import OneHotEncoder
onehot_encoder = OneHotEncoder(categorical_features = ['State'])
x = onehot_encoder.fit_transform(x).toarray()

# or
x = pd.get_dummies(x['gender'])
