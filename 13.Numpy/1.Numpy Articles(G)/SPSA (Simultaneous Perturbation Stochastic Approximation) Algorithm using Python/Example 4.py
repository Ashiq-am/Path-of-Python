def grad(L, w, ck):
    # number of parameters
    p = len(w)

    # bernoulli-like distribution
    deltak = np.random.choice([-1, 1], size=p)

    # simultaneous perturbations
    ck_deltak = ck * deltak

    # gradient approximation
    DELTA_L = L(w + ck_deltak) - L(w - ck_deltak)

    return (DELTA_L) / (2 * ck_deltak)
