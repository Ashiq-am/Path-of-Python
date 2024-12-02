import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="Sine Wave")
ax.set_title("Graph with Cross-Hair Cursor")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()

# Adding cross-hair functionality
def on_move(event):
    if event.inaxes:
        ax.lines = ax.lines[:1]  # Clear old cross-hair
        ax.axvline(event.xdata, color='red', linestyle='--')  # Vertical line
        ax.axhline(event.ydata, color='blue', linestyle='--')  # Horizontal line
        plt.draw()

fig.canvas.mpl_connect('motion_notify_event', on_move)
plt.show()