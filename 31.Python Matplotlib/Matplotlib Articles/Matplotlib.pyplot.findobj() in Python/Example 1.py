import matplotlib.pyplot as plt
import numpy as np

h = plt.figure()

plt.plot(range(1, 11),
         range(1, 11),
         gid='dummy_data')

legend = plt.legend(['the plotted line'])

plt.title('figure')

axis = plt.gca()
axis.set_xlim(0, 5)

for p in set(h.findobj(lambda x: x.get_gid() == 'dummy_data')):
    p.set_ydata(np.ones(10) * 10.0)

plt.show()
