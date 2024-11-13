# Graph using numpy.linspace()
# finding Skewness

from scipy.stats import skew
import numpy as np
import pylab as p

x1 = np.linspace( -5, 5, 1000 )
y1 = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x1)**2 )

p.plot(x1, y1, '*')

print( '\nSkewness for data : ', skew(y1))
