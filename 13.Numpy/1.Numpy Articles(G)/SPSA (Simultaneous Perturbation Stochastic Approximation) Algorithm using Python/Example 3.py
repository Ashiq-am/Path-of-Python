def Loss(parameters, X, Y):
    # Predictions of our model
    Y_pred = polynomial(parameters, X)

    # mse (mean square error)
    L = ((Y_pred - Y) ** 2).mean()

    # Noise in range: [-5, 5]
    noise = 5 * np.random.random()
    return L + noise
