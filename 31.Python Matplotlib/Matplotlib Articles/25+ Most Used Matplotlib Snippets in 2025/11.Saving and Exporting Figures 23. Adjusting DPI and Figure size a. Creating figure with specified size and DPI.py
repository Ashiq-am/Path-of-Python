import matplotlib.pyplot as plt

# Create a figure with specific size and DPI
plt.figure(figsize=(8, 6), dpi=100)     # 8 inches wide, 6 inches tall, 100 DPI
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('Figure with Custom Size and DPI')
plt.show()