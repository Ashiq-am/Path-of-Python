import matplotlib.pyplot as plt


def create_spiral(df, col_name='temperature', cycles=12, cmap='coolwarm'):
    # Create time index and normalize it to range from 0 to cycles * 2*pi
    time_index = np.linspace(0, 2 * np.pi * cycles, len(df))

    # Define the spiral equation parameters
    a = 0.1  # Starting radius
    b = 0.05  # Distance between turns

    # Spiral equation
    r = a + b * time_index
    theta = time_index

    # Temperature values to be mapped onto the spiral
    values = df[col_name].values

    # Plotting the spiral
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r, color='blue', alpha=0.5, label='Time')

    # Scatter the temperature values on the spiral
    scatter = ax.scatter(theta, r, c=values, cmap=cmap, label='Temperature')

    # Add color bar for temperature values
    plt.colorbar(scatter, ax=ax, orientation='vertical', label='Temperature')

    # Add labels and title
    plt.title('Spiral Time-Series Plot')
    plt.show()


# Call the function to create the spiral plot with random data
create_spiral(df, col_name='temperature', cycles=12)
