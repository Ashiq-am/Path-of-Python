from pybrain.optimization.populationbased.ga import GA

# GA optimization algorithm
gaOptimization = GA(orDataset.evaluateModuleMSE,
					myNetwork, minimize=True)
