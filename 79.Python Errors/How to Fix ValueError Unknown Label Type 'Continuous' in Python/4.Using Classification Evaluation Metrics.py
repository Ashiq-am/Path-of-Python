from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression

# Example data with continuous labels
X = [[0, 1], [1, 2], [2, 3], [3, 4]]
y = [0.5, 1.5, 2.5, 3.5]

# Convert continuous labels to discrete classes
y = [int(label) for label in y]

# Using Logistic Regression for classification
classifier = LogisticRegression()
classifier.fit(X, y)

# Predicting labels
y_pred = classifier.predict(X)

# Using classification evaluation metric instead of regression
accuracy = classifier.score(X, y)
print(accuracy)  # Using accuracy as an example
