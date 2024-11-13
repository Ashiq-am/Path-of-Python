from pyspark.ml.feature import StandardScaler

scaler = StandardScaler(inputCol="features",
						outputCol="scaledFeatures",
						withStd=True,
						withMean=False)

# Compute summary statistics by fitting the StandardScaler
scalerModel = scaler.fit(final_data)

# Normalize each feature to have unit standard deviation.
final_data = scalerModel.transform(final_data)

final_data.select('scaledFeatures').show(5)
