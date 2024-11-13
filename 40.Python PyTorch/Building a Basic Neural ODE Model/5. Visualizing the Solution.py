# Step 4: Visualizing the Solution
def plot_trajectory():
    t, y = solve_ode()                        # Solve the ODE and get the time and solution
    plt.plot(y[:, 0, 0].detach().numpy(), y[:, 0, 1].detach().numpy())  # Plot the trajectory
    plt.title('Trajectory of Neural ODE')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Call the function to visualize the solution
plot_trajectory()
