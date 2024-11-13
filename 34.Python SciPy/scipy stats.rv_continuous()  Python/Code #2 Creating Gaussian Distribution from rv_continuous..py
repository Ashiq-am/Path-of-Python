from scipy.stats import rv_continuous
import numpy as np


class gaussian_gen(rv_continuous):
    '''Gaussian distribution'''

    def _pdf(self, x):
        return np.exp(-x ** 2 / 2.) / np.sqrt(2.0 * np.pi)


gaussian = gaussian_gen(name='gaussian')

x = 2.0
gaussian._pdf(x)
