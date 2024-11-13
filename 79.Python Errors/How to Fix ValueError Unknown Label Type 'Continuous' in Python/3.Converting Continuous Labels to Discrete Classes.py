from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Example data with continuous labels
X = [[0, 1], [1, 2], [2, 3], [3, 4]]
y = [0.5, 1.5, 2.5, 3.5]

# Convert continuous labels to discrete classes
y = [int(label) for label in y]

# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Using Support Vector Classifier for classification
classifier = SVC()
classifier.fit(X_train, y_train)
print(classifier)
