import altair as alt
import pandas as pd

data = pd.DataFrame({
    'x': range(10),
    'y': range(10),
    'z': [i**2 for i in range(10)],  # Additional feature for color encoding
    'category': ['A', 'B'] * 5  # Categorical feature for shape encoding
})

chart = alt.Chart(data).mark_line(point=True).encode(
    x=alt.X('x:O', title='X Axis Label'),
    y=alt.Y('y:O', title='Y Axis Label'),
    color=alt.Color('z:Q', scale=alt.Scale(scheme='viridis'), title='Z Values'),
    shape=alt.Shape('category:N', title='Category'),
    tooltip=['x:O', 'y:O', 'z:Q', 'category:N']  # Adding tooltips for interactivity
).properties(
    title='Enhanced Altair Chart',
    width=600,
    height=400
).interactive()  # Enable zooming and panning

chart.save('enhanced_chart.html')
