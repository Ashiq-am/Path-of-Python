import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create example time series data
dates = pd.date_range('2023-01-01', periods=100)
data = {
    'Date': np.tile(dates, 3),
    'Value': np.concatenate([
        np.cumsum(np.random.randn(100)),
        np.cumsum(np.random.randn(100)),
        np.cumsum(np.random.randn(100))
    ]),
    'Series': np.repeat(['Series A', 'Series B', 'Series C'], 100)
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Loop through series and create line plots
series_list = df['Series'].unique()
for series in series_list:
    # Filter data for the current series
    subset = df[df['Series'] == series]

    # Create a new figure
    plt.figure(figsize=(10, 6))

    # Generate the line plot
    sns.lineplot(x='Date', y='Value', data=subset)

    # Set the title and labels
    plt.title(f'Line Plot for {series}')
    plt.xlabel('Date')
    plt.ylabel('Value')

    # Display the plot
    plt.show()
