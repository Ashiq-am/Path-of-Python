import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])

# Create a bytes buffer to save the plot
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# Open the PNG image from the buffer and convert it to a NumPy array
image = np.array(Image.open(buf))
# Close the buffer
buf.close()

print("Image shape:", image.shape)
print("First 3x3 pixels and RGB values:")
print(image[:3, :3, :])
