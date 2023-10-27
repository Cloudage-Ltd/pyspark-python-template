from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('Sample_Spark_App').getOrCreate()

df = spark.createDataFrame([('sample1', '31'), ('Ram', '40')], ('name', 'number'))

df.show()