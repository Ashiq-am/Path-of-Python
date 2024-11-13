from sklearn import datasets
from scipy.stats import entropy
import numpy as np

wine = datasets.load_wine()
X = wine.data
y = wine.target
y_entropy = entropy(np.bincount(y), base=2)
print("Entropy of Wine dataset (multiclass classification):", y_entropy)
