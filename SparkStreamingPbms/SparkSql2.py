from pyspark.sql import Row
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python SQL Basic Example").getOrCreate()
sc = spark.sparkContext

lines = sc.textFile("/Users/radhikagoel/WorkPlace/BigDataTech/spark-2.3.1-bin-hadoop2.7/examples/src/main/resources/people.txt")
parts = lines.map(lambda l: l.split(","))

people = parts.map(lambda p: Row(name=p[0],age=int(p[1])))

schemaPeople = spark.createDataFrame(people)

schemaPeople.createOrReplaceTempView("people")

teenagers = spark.sql("SELECT name FROM people WHERE age >= 13 AND age <= 19")

# The results of SQL queries are Dataframe objects.
# rdd returns the content as an :class:`pyspark.RDD` of :class:`Row`.
teenNames = teenagers.rdd.map(lambda p: "Name: " + p.name).collect()
for name in teenNames:
	print(name)
# Name: Justin