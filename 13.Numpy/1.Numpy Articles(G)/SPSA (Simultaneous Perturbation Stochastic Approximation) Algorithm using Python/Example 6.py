# optimization algorithm
def SPSA(LossFunction, parameters, alpha=0.602,
         gamma=0.101, N_iterations=int(1e5)):
    # model's parameters
    w = parameter

    a, A, c = initialize_hyperparameters(
        alpha, LossFunction, w, N_iterations)

    for k in range(1, N_iterations):
        # update ak and ck
        ak = a / ((k + A) ** (alpha))
        ck = c / (k ** (gamma))

        # estimate gradient
        gk = grad(LossFunction, w, ck)

        # update parameters
        w -= ak * gk

    return w
