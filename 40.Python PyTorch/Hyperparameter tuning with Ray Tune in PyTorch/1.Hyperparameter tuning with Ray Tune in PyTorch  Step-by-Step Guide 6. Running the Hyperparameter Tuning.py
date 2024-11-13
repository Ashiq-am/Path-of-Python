scheduler = ASHAScheduler(
    metric="loss",
    mode="min",
    max_t=10,
    grace_period=1,
    reduction_factor=2
)

result = tune.run(
    train_cifar,
    resources_per_trial={"cpu": 2, "gpu": 1},
    config=config,
    num_samples=10,
    scheduler=scheduler
)

print("Best config: ", result.get_best_config(metric="loss", mode="min"))
