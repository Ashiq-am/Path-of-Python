import pandas as pd
import altair as alt

# Sample DataFrame with non-positive values
df = pd.DataFrame({
    'group': ['A', 'B', 'C', 'D'],
    'value': [10, 0, -5, 100]
})

# Filter out non-positive values (values <= 0)
df_filtered = df[df['value'] > 0]

# Create a scatter plot with a logarithmic scale on the y-axis using the filtered DataFrame
chart = alt.Chart(df_filtered).mark_circle().encode(
    x='group',  # Group names on the x-axis
    y=alt.Y('value', scale=alt.Scale(type='log'))  # Logarithmic scale on y-axis
)

chart
