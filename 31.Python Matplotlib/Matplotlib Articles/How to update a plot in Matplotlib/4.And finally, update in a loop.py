for phase in np.linspace(0, 10*np.pi, 100):
	line1.set_ydata(np.sin(0.5 * x + phase))
	fig.canvas.draw()
	fig.canvas.flush_events()
