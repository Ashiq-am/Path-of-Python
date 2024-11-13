def solve_ode():
    func = ODEFunc()  # Instantiate the ODE function
    y0 = torch.tensor([[0.0, 1.0]])  # Initial hidden state (2D vector)
    t = torch.linspace(0, 25, 100)  # Time points to evaluate the solution
    y = odeint(func, y0, t)  # Solve the ODE

    # Print the time points and the corresponding ODE solution
    for i in range(len(t)):
        print(f"Time: {t[i].item()}, Solution: {y[i].detach().numpy()}")

    return t, y
