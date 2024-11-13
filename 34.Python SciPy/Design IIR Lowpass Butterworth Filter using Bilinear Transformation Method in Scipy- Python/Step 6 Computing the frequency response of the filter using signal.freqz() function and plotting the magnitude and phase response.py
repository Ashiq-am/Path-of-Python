# Compute frequency response of the filter using signal.freqz function
wz, hz = signal.freqz(z, p, 512)

# Plot filter magnitude and phase responses using subplot.
# Convert digital frequency wz into analog frequency in Hz
fig = plt.figure(figsize=(12, 10))

# Calculate Magnitude from hz in dB
Mag = 20*np.log10(abs(hz))

# Calculate frequency in Hz from wz
Freq = wz*Fs/(2*np.pi)

# Plot Magnitude response
sub1 = plt.subplot(2, 1, 1)
sub1.plot(Freq, Mag, 'r', linewidth=2)
sub1.axis([1, Fs/2, -60, 5])
sub1.set_title('Magnitute Response', fontsize=15)
sub1.set_xlabel('Frequency [Hz]', fontsize=15)
sub1.set_ylabel('Magnitude [dB]', fontsize=15)
sub1.grid()


# Plot phase angle
sub2 = plt.subplot(2, 1, 2)

# Calculate phace angle in degree from hz
Phase = np.unwrap(np.angle(hz))*180/np.pi
sub2.plot(Freq, Phase, 'g', linewidth=2)
sub2.set_ylabel('Phase (degree)', fontsize=15)
sub2.set_xlabel(r'Frequency (Hz)', fontsize=15)
sub2.set_title(r'Phase response', fontsize=15)
sub2.grid()

plt.subplots_adjust(hspace=0.5)
fig.tight_layout()
plt.show()
