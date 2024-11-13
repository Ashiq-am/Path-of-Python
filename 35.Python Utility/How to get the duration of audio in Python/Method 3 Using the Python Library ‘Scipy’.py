# Method 3
import scipy
from scipy.io import wavfile

# function to convert the information into
# some readable format
def output_duration(length):
	hours = length // 3600 # calculate in hours
	length %= 3600
	mins = length // 60 # calculate in minutes
	length %= 60
	seconds = length # calculate in seconds

	return hours, mins, seconds

# sample_rate holds the sample rate of the wav file
# in (sample/sec) format
# data is the numpy array that consists
# of actual data read from the wav file
sample_rate, data = wavfile.read('alarm.wav')

len_data = len(data) # holds length of the numpy array

t = len_data / sample_rate # returns duration but in floats

hours, mins, seconds = output_duration(int(t))
print('Total Duration: {}:{}:{}'.format(hours, mins, seconds))
