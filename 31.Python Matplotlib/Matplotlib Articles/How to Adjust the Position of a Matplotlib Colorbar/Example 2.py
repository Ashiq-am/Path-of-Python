#import matplotlib.pyplot to create chart
import matplotlib.pyplot as plt
import numpy as np

#create subplot
fig = plt.figure()
ax = fig.add_subplot(111)
axp = ax.imshow(np.random.randint(0, 10,( 10, 10)))
ax.set_title('Colorbar on left')

#adding colorbar and its position
cb = plt.colorbar(axp ,ax = [ax], location = 'left')
plt.show()
