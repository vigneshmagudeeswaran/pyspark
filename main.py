from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('practise').getOrCreate()

df_pyspark = spark.read.csv('csv_data.csv')
print(df_pyspark)
a = spark.read.option('header', 'true').csv('csv_data.csv').show()
print(a)