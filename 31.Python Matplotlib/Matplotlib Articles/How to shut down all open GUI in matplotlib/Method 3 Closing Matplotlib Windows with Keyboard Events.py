import matplotlib.pyplot as plt

def close_figure(event):
    if event.key == 'q':
        plt.close(event.canvas.figure)

fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', close_figure)
plt.plot([1, 2, 3])
plt.show()