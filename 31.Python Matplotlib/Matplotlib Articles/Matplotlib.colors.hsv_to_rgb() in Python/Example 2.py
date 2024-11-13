from matplotlib.colors import hsv_to_rgb

# sample squares for example
first_square = np.full((50, 50, 3),
					fill_value ='698',
					dtype = np.uint8) / 255.0

second_square = np.full((50, 50, 3),
						fill_value ='385',
						dtype = np.uint8) / 255.0

plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(first_square))

plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(second_square))

plt.show()
