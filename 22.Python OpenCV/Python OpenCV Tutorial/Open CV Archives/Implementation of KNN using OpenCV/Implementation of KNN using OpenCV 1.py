# generate a random data point
# unkown is a random data point for which we will perform prediction.
import cv as cv
from pandas import np
from pint.testsuite.test_matplotlib import plt
from pip._vendor.webencodings import labels

unknown = np.random.randint(0, 50, (1, 2)).astype(np.float32)
# create the knn classifier
knn = cv.ml.KNearest_create()

# we use cv.ml.ROW_SAMPLE to occupy a row of samples from the samples.
knn.train(Data_points, cv.ml.ROW_SAMPLE, labels)
# get the labelled result, the numbers, the distance of each data point.
# find nearest finds the specified number of neighbours and predicts responses.
ret, res, neighbours, distance = knn.findNearest(unknown, 5)

# For each row of samples the method finds the k nearest neighbours.
# For regression problems, the predicted result is a mean of all the neighbours.
# For classification, the class is determined by the majority.

# plot the data point with other data points
plt.scatter(unknown[:, 0], unknown[:, 1], 80, 'g', '^')
# show the result.
plt.show()

# print the results obtained
print( "Label of the unknown data - ", res )
print( "Nearest neighbors - ", neighbours )
print( "Distance of each neighbor - ", distance )
