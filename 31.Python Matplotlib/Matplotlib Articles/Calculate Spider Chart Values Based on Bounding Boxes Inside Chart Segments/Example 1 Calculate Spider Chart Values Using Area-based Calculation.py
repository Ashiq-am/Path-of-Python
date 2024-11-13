import matplotlib.pyplot as plt
import numpy as np


def GFG(bounding_boxes):
    """Calculate spider chart values based on bounding boxes."""
    total_area = sum(box_area(box) for box in bounding_boxes)
    spider_chart_values = [
        box_area(box) / total_area for box in bounding_boxes]
    return spider_chart_values


def box_area(box):
    """Calculate the area of a bounding box."""
    return (box[2] - box[0]) * (box[3] - box[1])


# Sample bounding boxes
bounding_boxes = [(10, 20, 50, 80), (40, 30, 70, 60), (70, 25, 110, 65)]
spider_chart_values = GFG(bounding_boxes)

# Define categories and angles for the spider chart
categories = ['Category 1', 'Category 2', 'Category 3']
num_categories = len(categories)
angles = np.linspace(0, 2 * np.pi, num_categories, endpoint=False).tolist()

# Plot spider chart
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
ax.fill(angles, spider_chart_values, color='blue', alpha=0.25)
ax.plot(angles, spider_chart_values, color='blue',
        linewidth=2, linestyle='solid')
ax.set_yticklabels([])
ax.set_xticks(angles)
ax.set_xticklabels(categories)
ax.set_title('Spider Chart')

plt.show()
