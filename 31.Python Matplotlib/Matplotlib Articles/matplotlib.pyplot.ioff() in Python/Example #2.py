# Implementation of matplotlib function
import matplotlib.pyplot as plt
import numpy as np

plt.ioff()
random_array = np.arange(-2, 4)
line_1 = random_array * 2
line_2 = 10 / (random_array * 2 + 1)
figure, axes = plt.subplots()

axes.plot(random_array, line_1,
          'ro-', random_array,
          line_2, 'bo-',
          linestyle='solid')

axes.fill_between(random_array,
                  line_1,
                  line_2,
                  where=line_2 > line_1,
                  interpolate=True,
                  color='green', alpha=0.4)

lgnd = axes.legend(['line-1',
                    'line-2'],
                   loc='lower center',
                   shadow=True)

lgnd.get_frame().set_facecolor('# ffb19a')
plt.title('matplotlib.pyplot.ioff() function Example',
          fontweight="bold")
plt.show()
