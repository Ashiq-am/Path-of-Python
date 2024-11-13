import matplotlib

# changing backend
from IPython.terminal.pt_inputhooks import tk

matplotlib
tk
import matplotlib.pyplot as plt

# saving the figure
plt.savefig('testfigure.png',
			dpi = 100)

# displaying the figure
plt.show()
