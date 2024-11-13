#Importing the model
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

silhouette_score=[]

evaluator = ClusteringEvaluator(predictionCol='prediction',
								featuresCol='scaledFeatures', \
								metricName='silhouette',
								distanceMeasure='squaredEuclidean')

for i in range(2,10):
	kmeans=KMeans(featuresCol='scaledFeatures', k=i)
	model=kmeans.fit(final_data)
	predictions=model.transform(final_data)
	score=evaluator.evaluate(predictions)
	silhouette_score.append(score)
	print('Silhouette Score for k =',i,'is',score)
