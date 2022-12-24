from pyspark.sql import SparkSession


# if __name__ == '__main__':
print('Hello world')

spark = SparkSession.builder.appName('Sample_Spark_App').getOrCreate()

df = spark.createDataFrame([('ram', '31')], ('name', 'number'))

df.show()