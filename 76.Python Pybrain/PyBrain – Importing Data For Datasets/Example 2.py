from pybrain.datasets import ClassificationDataSet
from sklearn import datasets

nums = datasets.load_iris()
x, y = nums.data, nums.target
ds = ClassificationDataSet(4, 1, nb_classes=3)
for j in range(len(x)):
	ds.addSample(x[j], y[j])
ds
