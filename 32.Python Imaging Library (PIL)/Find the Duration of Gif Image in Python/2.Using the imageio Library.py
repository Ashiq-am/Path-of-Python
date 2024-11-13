# import the module
import imageio

# read the GIF file
gif = imageio.get_reader("input.gif")

# Initialize the duration
duration = 0

# Loop through the frames and sum the durations
for frame in gif:
    duration += gif.get_meta_data(index=frame)["duration"]

    # Print the total duration in milliseconds
print(f"Total duration: {duration} ms")
