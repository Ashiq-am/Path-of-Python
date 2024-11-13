# Function to calculate basic statistics
def channel_statistics(channel):
    mean = np.mean(channel)
    median = np.median(channel)
    std_dev = np.std(channel)
    min_val = np.min(channel)
    max_val = np.max(channel)
    return mean, median, std_dev, min_val, max_val


# Calculate statistics for each channel
stats = {}
for channel, color in zip(channels, colors):
    stats[color] = channel_statistics(channel)

print('RGB Channel Statistics:')
for color, stat in stats.items():
    print(
        f'{color.capitalize()} Channel - Mean: {stat[0]:.2f}, Median: {stat[1]:.2f}, Std Dev: {stat[2]:.2f}, Min: {stat[3]}, Max: {stat[4]}')
