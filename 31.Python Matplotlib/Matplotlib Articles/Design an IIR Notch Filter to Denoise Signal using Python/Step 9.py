# Plot notch-filtered version of signal
plt.subplot(212)

# Plot output signal of notch filter
plt.plot(n, outputSignal)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Magnitude', fontsize=18)
plt.title('Filtered Signal', fontsize=20)
plt.subplots_adjust(hspace=0.5)
fig.tight_layout()
plt.show()
