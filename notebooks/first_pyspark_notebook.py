
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FirstNotebook").getOrCreate()
df = spark.createDataFrame([("Anna", 25)], ["Name", "Age"])
df.show()
