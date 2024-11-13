# Fill Null values inside Department column with the word 'Generalist'
df_pyspark.na.fill('Generalist',subset=['Department']).show()
