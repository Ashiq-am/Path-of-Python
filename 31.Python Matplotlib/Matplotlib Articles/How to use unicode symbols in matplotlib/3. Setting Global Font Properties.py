import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set global font properties
rcParams['font.family'] = 'DejaVu Sans'  # Ensure the font supports Unicode
uni_star = u"\u2739"  # Star symbol
uni_heart = u"\u2764"  # Heart symbol
uni_arrow = u"\u2192"  # Arrow symbol

plt.figure(figsize=(8, 3))

plt.text(0.3, 0.7, f"Star: {uni_star}", fontsize=20, ha='center')
plt.text(0.7, 0.7, f"Heart: {uni_heart}", fontsize=20, ha='center')
plt.text(0.5, 0.4, f"Arrow: {uni_arrow}", fontsize=25, ha='center', color='blue')

plt.title(f"Title with Unicode {uni_heart}", fontsize=18)
plt.xlabel(f"X-axis {uni_arrow}", fontsize=15)
plt.ylabel(f"Y-axis {uni_star}", fontsize=15)

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid(True)
plt.show()