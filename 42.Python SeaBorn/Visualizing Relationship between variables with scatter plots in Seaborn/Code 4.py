sns.relplot(x ="ENGINESIZE", y ="CO2EMISSIONS",
			hue ="FUELTYPE", style ="FUELTYPE",
			data = dataset);
