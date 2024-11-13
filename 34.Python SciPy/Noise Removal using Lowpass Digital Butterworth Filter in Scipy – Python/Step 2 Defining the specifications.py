# Specifications of the filter
f1 = 25 # Frequency of 1st signal
f2 = 50 # Frequency of 2nd signal
N = 10 # Order of the filter


# Generate the time vector of 1 sec duration
t = np.linspace(0, 1, 1000) # Generate 1000 samples in 1 sec

# Generate the signal containing f1 and f2
sig = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)
