from pyspark.ml.feature import VectorAssembler

assembler = VectorAssembler(
    inputCols=['Avg Session Length', "Time on App", "Time on Website", 'Length of Membership'],
    outputCol="features")

output = assembler.transform(df)
output.select("features").show(5)
