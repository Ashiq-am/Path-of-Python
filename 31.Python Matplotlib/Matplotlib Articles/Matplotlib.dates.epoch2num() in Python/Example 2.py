from tkinter import *
from tkinter import ttk
import time
import matplotlib
import queue
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.dates as mdate

root = Tk()

graphXData = queue.Queue()
graphYData = queue.Queue()


def animate(objData):
    line.set_data(list(graphXData.queue),
                  list(graphYData.queue))

    axes.relim()
    axes.autoscale_view()


figure = Figure(figsize=(5, 5), dpi=100)
axes = figure.add_subplot(111)
axes.xaxis_date()

line, = axes.plot([], [])
axes.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack(side=BOTTOM,
                            fill=BOTH,
                            expand=True)

for cnt in range(600):
    graphXData.put(matplotlib.dates.epoch2num(time.time() - (600 - cnt)))
    graphYData.put(0)

ani = animation.FuncAnimation(figure, animate, interval=1000)

root.mainloop()
