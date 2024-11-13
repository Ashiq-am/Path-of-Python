flat_image = image.reshape(-1, 3)
print("First 10 pixels (flattened):")
for i in range(10):
    print(f"Pixel {i+1} (R value, G value, B value): {flat_image[i]}")
