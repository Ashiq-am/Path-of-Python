import numpy as np
import matplotlib.pyplot as plt

distribution = np.linspace(levy_stable.ppf(0.01, 1.8, -0.5),
                           levy_stable.ppf(0.99, 1.8, -0.5), 100)
print("Distribution : \n", distribution)
