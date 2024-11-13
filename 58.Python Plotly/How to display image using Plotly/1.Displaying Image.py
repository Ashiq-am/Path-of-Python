import plotly.express as px
import numpy as np


# RGB Data as numpy array
img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
					], dtype=np.uint8)

fig = px.imshow(img_rgb)
fig.show()
