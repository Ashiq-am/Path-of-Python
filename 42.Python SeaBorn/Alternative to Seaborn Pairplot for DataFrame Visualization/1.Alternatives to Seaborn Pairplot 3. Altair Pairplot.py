import altair as alt
from vega_datasets import data
import pandas as pd

df = data.cars()

# Define the columns to include in the pairplot
columns = ['Horsepower', 'Miles_per_Gallon', 'Acceleration', 'Displacement']

# Create a pairplot using the repeat operator
chart = alt.Chart(df).mark_point().encode(
    alt.X(alt.repeat("column"), type="quantitative"),
    alt.Y(alt.repeat("row"), type="quantitative"),
    color='Origin:N'
).properties(
    width=200,
    height=200
).repeat(
    row=columns,
    column=columns
).interactive()

chart
