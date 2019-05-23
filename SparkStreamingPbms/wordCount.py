from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split


# import pyspark
# from pyspark import SparkContext, SparkConf
#
# conf = SparkConf().setAppName("Pyspark_pgm")
# sc = SparkContext(conf = conf)
# contentRDD = sc.textFile("myfile")
# nonempty_lines = contentRDD.filter(lambda x:len(x) > 0)
# words = nonempty_lines.flatMap(lambda x:x.split(' '))

#wordcount = words.map(lambda x:(x,1)) .reduceByKey(lambda x,y: x+y) .map(lambda x: (x[1], x[0])).sortByKey(False)
#for word in wordcount.collect():
#	print (word)

spark = SparkSession.builder.appName("StreamingWordCount").getOrCreate()
lines = spark.readStream.format("socket").option("host","localhost").option("port",9999).load()

words = lines.select(explode(split(lines.value, " ")).alias("word"))
wordCounts = words.groupBy("word").count()



query = wordCounts.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()

