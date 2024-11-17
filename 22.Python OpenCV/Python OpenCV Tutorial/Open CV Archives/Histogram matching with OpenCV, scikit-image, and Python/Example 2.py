# importing packages
import matplotlib.pyplot as plt
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms

# loading data
reference = data.moon()
image = data.camera()

# matching histograms
matched = match_histograms(image, reference,
						multichannel=True,)

fig, (ax1, ax2, ax3) = plt.subplots(nrows=1,
									ncols=3,
									figsize=(8, 3),
									sharex=True,
									sharey=True)
for aa in (ax1, ax2, ax3):
	aa.set_axis_off()

# displaying images
ax1.imshow(image)
ax1.set_title('Source image')
ax2.imshow(reference)
ax2.set_title('Reference image')
ax3.imshow(matched)
ax3.set_title('Matched image')

plt.tight_layout()
plt.show()
