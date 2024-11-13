import altair as alt
from vega_datasets import data

iris = data.iris()

chart = alt.Chart(iris).mark_point().encode(
    x='petalWidth',
    y=alt.Y('petalLength', axis=alt.Axis(labels=False, ticks=False)),
    color='species'
)
chart
