from pyspark.ml.feature import VectorAssembler

vec_assembler = VectorAssembler(inputCols = dataset.columns,
								outputCol='features')

final_data = vec_assembler.transform(dataset)
final_data.select('features').show(5)
