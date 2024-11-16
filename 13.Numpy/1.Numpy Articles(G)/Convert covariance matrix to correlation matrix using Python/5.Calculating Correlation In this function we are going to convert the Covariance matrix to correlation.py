# Now calculating Correlation using our Covariance function (covMat())
from pandas import np


def corrMat(data):
    rows, cols = data.shape

    corr_mat = np.zeros((cols, cols))

    for i in range(cols):

        for j in range(cols):
            x, y = data[:, i], data[:, j]
            # not here that we are just normalizing the covariance matrix
            corr_mat[i][j] = calcCov(x, y) / (x.std() * y.std())

    return corr_mat


corrMat(data)


