# Importing all the necessary libraries
from sklearn import datasets
import matplotlib.pyplot as plt
from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer
from numpy import ravel

# Loading iris dataset from sklearn datasets
iris = datasets.load_iris()

# Defining feature variables and target variable
X_data = iris.data
y_data = iris.target

# Defining classification dataset model
classification_dataset = ClassificationDataSet(4, 1, nb_classes=3)

# Adding sample into classification dataset
for i in range(len(X_data)):
	classification_dataset.addSample(ravel(X_data[i]), y_data[i])

# Spilling data into testing and training data
# with the ratio 7:3
testing_data, training_data = classification_dataset.splitWithProportion(0.3)

# Classification dataset for test data
test_data = ClassificationDataSet(4, 1, nb_classes=3)

# Adding sample into testing classification dataset
for n in range(0, testing_data.getLength()):
	test_data.addSample(testing_data.getSample(
		n)[0], testing_data.getSample(n)[1])

# Classification dataset for train data
train_data = ClassificationDataSet(4, 1, nb_classes=3)

# Adding sample into training classification dataset
for n in range(0, training_data.getLength()):
	train_data.addSample(training_data.getSample(
		n)[0], training_data.getSample(n)[1])

test_data._convertToOneOfMany()
train_data._convertToOneOfMany()

# Building network with outclass as SoftmaxLayer
# on training data
build_network = buildNetwork(
	train_data.indim, 4, train_data.outdim, outclass=SoftmaxLayer)

# Building a backproptrainer on training data
trainer = BackpropTrainer(
	build_network, dataset=train_data, learningrate=0.01, verbose=True)

# 20 iterations on training data
trainer.trainEpochs(20)

# Testing data
print('Error percentage on testing data=>', percentError(
	trainer.testOnClassData(dataset=test_data), test_data['class']))
