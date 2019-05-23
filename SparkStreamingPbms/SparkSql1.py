from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python SQL Basic Example").getOrCreate()
df = spark.read.json("/Users/radhikagoel/WorkPlace/BigDataTech/spark-2.3.1-bin-hadoop2.7/examples/src/main/resources/people.json")
df.show()

df.printSchema()

df.select('name').show()

df.select(df['name'],df['age'] + 1).show()

df.filter(df['age'] > 21).show()

df.groupBy('age').count().show()


df.createOrReplaceTempView("people")

sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()