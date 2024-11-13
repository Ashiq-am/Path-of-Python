import numpy as np
import matplotlib.pyplot as plt

spike = 100*np.random.random(100)
plt.eventplot(spike,
			orientation = 'vertical',
			linelengths = 0.8,
			color = [(0.5,0.5,0.8)])
