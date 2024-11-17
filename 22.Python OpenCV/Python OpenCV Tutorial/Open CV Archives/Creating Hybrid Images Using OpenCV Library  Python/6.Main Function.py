# Load images
# Make sure to choose the same image format for both images (Ex- .png)
A = cv2.imread('/content/cat.png',cv2.IMREAD_COLOR) # high picture
B = cv2.imread('/content/panda.png',cv2.IMREAD_COLOR) # low picture

# Convert both images to Grayscale to avoid any Color Channel Issue
A_grayscale = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY)
B_grayscale = cv2.cvtColor(B, cv2.COLOR_BGR2GRAY)

# Resize both images to 128x128 to avoid different image size issue
A_resized = cv2.resize(A_grayscale, (128, 128))
B_resized = cv2.resize(B_grayscale, (128, 128))

result = hybrid_images(A_resized,B_resized,1)

plot_figure([A,B,result], ['A','B','Hybrid Image'],1,3)
