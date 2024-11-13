# Performing normaltest
from scipy.stats import normaltest
import numpy as np
import pylab as p

x1 = np.linspace( -5, 12, 1000 )
y1 = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x1)**2 )

p.plot(x1, y1, '.')

print( '\nNormal test for given data :\n', normaltest(y1))
