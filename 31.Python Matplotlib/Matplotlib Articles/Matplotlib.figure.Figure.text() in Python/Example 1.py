# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fig.text(0.28, 0.5,
         'GeeksforGeeks',
         style='italic',
         fontsize=30,
         color="green")

ax.set(xlim=(0, 8),
       ylim=(0, 8))

fig.suptitle("""matplotlib.figure.Figure.text() 
function Example\n\n""", fontweight="bold")

fig.show()
