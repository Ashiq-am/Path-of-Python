import seaborn.objects as so
import pandas as pd

# Sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
})

# Create and customize the plot
plot = (
    so.Plot(data)
    .add(so.Line(color='blue'), x='x', y='y')
    .add(so.Dot(), x='x', y='y')
    .label(x='Index', y='Value', title='Prime Numbers')
)

# Render the plot
plot.show()
