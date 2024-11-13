config = {
    "l1": tune.choice([2 ** i for i in range(7, 10)]),
    "l2": tune.choice([2 ** i for i in range(7, 10)]),
    "lr": tune.loguniform(1e-4, 1e-1),
    "batch_size": tune.choice([2, 4, 8, 16])
}
