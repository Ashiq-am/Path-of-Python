# Method 3: Adjusting Color Limits
plt.subplot(233)
plt.imshow(data, cmap='viridis', vmin=0.3, vmax=0.7)
plt.colorbar()
plt.title('Color Limits: 0.3 to 0.7')
plt.show()
