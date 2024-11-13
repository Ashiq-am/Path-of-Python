# Method 4: Using Colorbars
plt.subplot(234)
img = plt.imshow(data, cmap='plasma')
plt.colorbar(img, orientation='horizontal')
plt.title('Colorbar')
plt.show()
