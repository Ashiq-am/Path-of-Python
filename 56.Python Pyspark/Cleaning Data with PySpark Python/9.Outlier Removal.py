# Remove Outlier -- We assume 59 to be maximum working age in the company
df_pyspark.filter('Age<60').show()
