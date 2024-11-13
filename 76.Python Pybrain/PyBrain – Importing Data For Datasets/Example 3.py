from sklearn import datasets
from pybrain.datasets import ClassificationDataSet

digits = datasets.load_digits()
X, y = digits.data, digits.target
ds = ClassificationDataSet(64, 1, nb_classes=10)
for i in range(len(X)):
	ds.addSample(ravel(X[i]), y[i])
