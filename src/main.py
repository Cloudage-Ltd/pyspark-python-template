from pyspark.sql import SparkSession


spark = SparkSession.builder.appName('Sample_Spark_App').getOrCreate()

df = spark.createDataFrame([('sample', '31')], ('name', 'number'))

df.show()