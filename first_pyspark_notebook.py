
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("FirstNotebook").getOrCreate()

data = [("Anna", 25), ("John", 30)]
df = spark.createDataFrame(data, ["Name", "Age"])

df.show()
