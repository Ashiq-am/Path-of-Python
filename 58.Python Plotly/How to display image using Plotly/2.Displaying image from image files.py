import plotly.express as px
import cv2

# You can give path to the
# image as first argument
img = cv2.imread('GFG.png')

fig = px.imshow(img)
fig.show()
