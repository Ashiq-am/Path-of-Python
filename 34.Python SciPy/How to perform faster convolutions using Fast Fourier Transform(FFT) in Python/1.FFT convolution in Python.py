from scipy import signal

a = [1, 2, 3]
b = [4, 5, 6]

y = signal.fftconvolve(a, b, mode = 'full')
print('The convoluted sequence is ', y)
