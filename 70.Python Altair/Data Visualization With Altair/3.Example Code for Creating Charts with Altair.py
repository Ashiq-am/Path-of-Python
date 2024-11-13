import altair as alt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris_data = load_iris()
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
print(iris_df.columns)
# Scatter plot with hover (tooltip)
scatter_plot = alt.Chart(iris_df).mark_point().encode(
    x=alt.X('sepal length (cm)', axis=alt.Axis(title='Sepal Length (cm)')),
    y=alt.Y('sepal width (cm)', axis=alt.Axis(title='Sepal Width (cm)')),
    color='species',
    tooltip=['species', 'sepal length (cm)', 'sepal width (cm)']  # Tooltip on hover
).properties(
    title='Iris Dataset: Sepal Length vs Sepal Width'
)
scatter_plot.display()

# Bar chart to show average petal length per species
bar_chart = alt.Chart(iris_df).mark_bar().encode(
    x='species:N',
    y='mean(petal length (cm)):Q',
    color='species:N'
).properties(
    title='Average Petal Length by Species'
)
bar_chart.display()


# Histogram to show distribution of sepal width
histogram = alt.Chart(iris_df).mark_bar().encode(
    alt.X('sepal width (cm):Q', bin=True, title='Sepal Width'),
    y='count()',
    color='species:N'
).properties(
    title='Distribution of Sepal Width by Species'
)
histogram.display()

# Box plot for petal length by species
box_plot = alt.Chart(iris_df).mark_boxplot().encode(
    x='species:N',
    y='petal length (cm):Q',
    color='species:N'
).properties(
    title='Box Plot of Petal Length by Species'
)
box_plot.display()

# Create a selection object
selection = alt.selection_multi(fields=['species'], bind='legend')  # Multi-select based on species

# Scatter plot with hover and linked selection
scatter_plot = alt.Chart(iris_df).mark_point().encode(
    x=alt.X('sepal length (cm)', axis=alt.Axis(title='Sepal Length (cm)')),
    y=alt.Y('sepal width (cm)', axis=alt.Axis(title='Sepal Width (cm)')),
    color=alt.condition(selection, 'species:N', alt.value('lightgray')),  # Highlight selected species
    tooltip=['species', 'sepal length (cm)', 'sepal width (cm)']
).add_selection(
    selection  # Add the selection to the scatter plot
).properties(
    title='Iris Dataset: Sepal Length vs Sepal Width'
)

# Bar chart with linked selection
bar_chart = alt.Chart(iris_df).mark_bar().encode(
    x='species:N',
    y='mean(petal length (cm)):Q',
    color=alt.condition(selection, 'species:N', alt.value('lightgray'))  # Highlight selected species
).properties(
    title='Average Petal Length by Species'
).add_selection(
    selection  # Add the same selection to the bar chart
)

# Combine the charts vertically
combined_chart = alt.hconcat(bar_chart, scatter_plot)

# Display the combined chart
combined_chart.display()
