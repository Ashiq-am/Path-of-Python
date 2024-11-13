# Step 2: Generate Synthetic Data
def generate_data():
    # Create initial condition and time points
    y0 = torch.tensor([[0.0, 1.0]])  # Initial condition (2D vector)
    t = torch.linspace(0, 25, 100)   # Time points
    true_y = torch.sin(t).unsqueeze(1)  # True sine wave as target for training

    # Pack data into a dictionary
    data = {
        'y0': y0,
        't': t,
        'y_true': true_y
    }
    return data
