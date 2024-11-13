# Plot histograms
plt.figure(figsize=(15, 5))
colors = ['red', 'green', 'blue']
channels = [R, G, B]

for i, (channel, color) in enumerate(zip(channels, colors)):
    plt.subplot(1, 3, i+1)
    plt.hist(channel.ravel(), bins=256, color=color, alpha=0.8)
    plt.title(f'{color.capitalize()} Channel Histogram')
    plt.xlabel('Intensity Value')
    plt.ylabel('Frequency')

plt.show()
