# Adding font properties to labels and titles
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# Number of Childerns
x = np.array([0, 1, 2, 3])

# Number of Families
y = np.array([3, 8, 1, 10])

# label including this form1 will have these properties
form1 = {'family': 'serif', 'color': 'blue', 'size': 20}

# label including this form2 will have these properties
form2 = {'family': 'serif', 'color': 'darkred', 'size': 15}

plt.plot(x, y)
plt.xlabel("Number of Childerns", fontdict=form1)
plt.ylabel("Number of Families", fontdict=form1)
plt.title("Survey Of Colony", fontdict=form2)
plt.show()
