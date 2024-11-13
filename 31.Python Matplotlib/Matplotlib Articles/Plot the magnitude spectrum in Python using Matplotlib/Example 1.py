# importing modules
import numpy
from matplotlib import pyplot

# assigning time values of the signal
# initial time period, final time period and phase angle
signalTime = numpy.arange(5, 10, 0.25)

# getting the amplitude of the signal
signalAmplitude = numpy.sin(signalTime)

# plotting the signal
pyplot.plot(signalTime, signalAmplitude, color ='green')

pyplot.xlabel('Time')
pyplot.ylabel('Amplitude')
pyplot.title("Signal")


# plotting the magnitude spectrum of the signal
pyplot.magnitude_spectrum(signalAmplitude, color ='green')

pyplot.title("Magnitude Spectrum of the Signal")
pyplot.show()
