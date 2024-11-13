# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)
axes = axes.flatten()
for i in range(4):
    fig.sca(axes[i])
    axes[i].text(0.5, 0.5, i + 1)

fig.suptitle("""matplotlib.figure.Figure.sca() 
function Example\n\n""", fontweight="bold")

plt.show()
