from pybrain.datasets import SupervisedDataSet

DS = SupervisedDataSet(3, 2)
DS.appendLinked([1, 2, 3], [4, 5])
len(DS)
DS['input']
array([[1., 2., 3.]])
