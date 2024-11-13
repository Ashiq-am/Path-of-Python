# import pillow module
from PIL import Image

# open the GIF file
img = Image.open("input.gif")

# initialize the duration
duration = 0

# loop through the frames and add the durations
while True:
    try:
        frame_duration = img.info['duration']
        duration += frame_duration
        img.seek(img.tell() + 1)
    except EOFError:
        break

# printing the total duration in milliseconds
print(f"Total duration: {duration} ms")
