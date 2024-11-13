# Magnitude Response
plt.semilogx(w, 20*np.log10(abs(h)))
plt.xscale('log')

plt.title('Butterworth filter frequency response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, 0.1)

plt.grid(which='both', axis='both')
plt.axvline(100, color='green')
plt.show()
