import seaborn.objects as so
import pandas as pd

data = pd.DataFrame({
    'x': range(10),
    'y': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
})

# Create the plot
p = (
    so.Plot(data, x='x', y='y')
    .add(so.Line())
    .add(so.Dot(), color='y')
)
p.show()
