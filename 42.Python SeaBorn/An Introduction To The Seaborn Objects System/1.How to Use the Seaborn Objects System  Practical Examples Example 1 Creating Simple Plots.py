import seaborn.objects as so
import pandas as pd

# Sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
})

# Create the plot using Seaborn Objects
plot = (
    so.Plot(data)
    .add(so.Line(), x='x', y='y')
)

# Render the plot
plot.show()
