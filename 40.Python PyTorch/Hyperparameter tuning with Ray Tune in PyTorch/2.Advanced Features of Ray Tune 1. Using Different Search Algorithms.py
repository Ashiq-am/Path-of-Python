from ray.tune.search.optuna import OptunaSearch

algo = OptunaSearch()
tuner = tune.Tuner(
    train_cifar,
    tune_config=tune.TuneConfig(
        search_alg=algo,
        num_samples=10,
        metric="loss",
        mode="min"
    ),
    param_space=config
)

results = tuner.fit()
print("Best config: ", results.get_best_result().config)
