counter = 0

print("RGB values of the first 10 pixels:")
for row in range(height):
    for col in range(width):
        if counter < 10:
            r, g, b = image[row, col]
            print(f"Pixel {counter + 1} at (row {row}, col {col}): [{r}, {g}, {b}]")
            counter += 1
        else:
            break
    if counter >= 10:
        break
