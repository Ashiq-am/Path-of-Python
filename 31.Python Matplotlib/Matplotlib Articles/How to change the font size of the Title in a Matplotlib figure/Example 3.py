# importing modules
from matplotlib import pyplot
import numpy

# assigning time values of the signal
# initial time period, final time period
# and phase angle
signalTime = numpy.arange(0, 100, 0.5)

# getting the amplitude of the signal
signalAmplitude = numpy.sin(signalTime)

# depicting the visualization
pyplot.plot(signalTime, signalAmplitude,
			color = 'green')

pyplot.xlabel('Time')
pyplot.ylabel('Amplitude')

# displaying the title
pyplot.title("Signal",
			fontsize = 30)
