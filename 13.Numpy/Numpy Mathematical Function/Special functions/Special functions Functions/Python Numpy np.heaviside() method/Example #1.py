''''''


'''In this example we can see that by using np.heaviside() method, we are able to get the array of 
series of heaviside step function by using this method.'''






# import numpy
import numpy as np

x = np.array([-1.5, 0.5, 0, 0.5, 1.5])
# using np.heaviside() method
gfg = np.heaviside(x, 0.5)

print(gfg)
