import seaborn.objects as so
import pandas as pd

# Sample data
data = pd.DataFrame({
    'x': range(10),
    'y1': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
    'y2': [29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
})

# Create the plot with multiple layers
plot = (
    so.Plot(data)
    .add(so.Line(), x='x', y='y1')
    .add(so.Dot(), x='x', y='y2')
    .label(x='Index', y='Value', title='Multiple Layers Example')
)

# Render the plot
plot.show()
