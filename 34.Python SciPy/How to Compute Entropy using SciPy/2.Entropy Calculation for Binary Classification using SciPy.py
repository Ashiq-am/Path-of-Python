from sklearn import datasets
from scipy.stats import entropy
import numpy as np

iris = datasets.load_iris()
X = iris.data

# For simplicity, we'll classify the Iris species into two classes: Setosa (class 0) and Non-Setosa (class 1)
y = (iris.target != 0).astype(int)  # Setosa (class 0) vs Non-Setosa (class 1)
y_entropy = entropy(np.bincount(y), base=2) # Compute the entropy of the target variable (y)
print("Entropy of Iris dataset (binary classification):", y_entropy)
