import matplotlib.pyplot as plt
import numpy as np


def GFG(bounding_boxes, chart_segment):
    """
    Calculate the spider chart values for given bounding boxes and chart segment.
    """
    total_segment_area = chart_segment_area(chart_segment)
    intersection_areas = [box_segment_intersection(
        box, chart_segment) for box in bounding_boxes]
    spider_chart_values = [
        area / total_segment_area for area in intersection_areas]
    return spider_chart_values


def chart_segment_area(segment):
    """
    Calculate the area of a chart segment.
    """
    return (segment[2] - segment[0]) * (segment[3] - segment[1])  # (right - left) * (bottom - top)


def box_segment_intersection(box, segment):
    """
    Calculate the intersection area between a box and a chart segment.
    """
    intersect_left = max(box[0], segment[0])
    intersect_right = min(box[2], segment[2])
    intersect_top = max(box[1], segment[1])
    intersect_bottom = min(box[3], segment[3])
    if intersect_left < intersect_right and intersect_top < intersect_bottom:
        return (intersect_right - intersect_left) * (intersect_bottom - intersect_top)
    return 0


bounding_boxes = [(10, 20, 50, 80), (40, 30, 70, 60), (70, 25, 110, 65)]
chart_segment = (0, 0, 100, 100)
spider_chart_values = GFG(bounding_boxes, chart_segment)

# Print calculation
print("Spider chart values:", spider_chart_values)

# Spider chart parameters
labels = ['Box 1', 'Box 2', 'Box 3']
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values = spider_chart_values

# Create the spider chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)

# Add labels
ax.set_yticklabels([])
ax.set_xticks(angles)
ax.set_xticklabels(labels, fontsize=12)
plt.show()
