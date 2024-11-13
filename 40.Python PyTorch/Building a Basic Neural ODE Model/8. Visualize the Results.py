# Step 4: Visualizing the Results
def plot_results(model, data):
    with torch.no_grad():
        pred_y = odeint(model, data['y0'], data['t'])
        plt.plot(data['t'].numpy(), data['y_true'].numpy(), label='True')
        plt.plot(data['t'].numpy(), pred_y.squeeze().numpy(), '--', label='Predicted')
        plt.legend()
        plt.title('True vs Predicted Neural ODE')
        plt.show()
