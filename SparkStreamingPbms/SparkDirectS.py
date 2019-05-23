from pyspark import SparkContext
import json
from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import os

#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 pyspark-shell'


sc = SparkContext(appName = 'testSparkStreaming')
sc.setLogLevel("WARN")
ssc = StreamingContext(sc,2)

brokers = "localhost:2181"
#directKafkastream = KafkaUtils.createDirectStream(ssc, ["monitor"], {"metadata.broker.list": brokers})
topic="monitor"
directKafkastream = KafkaUtils.createStream(ssc,brokers,'test-consumer-group',{topic:1})

lines = directKafkastream.map(lambda x: x[1])
lines.pprint()
# offsetRanges = []
#
# def storeOffsetRanges(rdd):
# 	global offsetRanges
# 	offsetRanges = rdd.offsetRanges()
# 	return rdd
#
# def printOffsetRanges(rdd):
# 	print(offsetRanges)
# 	for o in offsetRanges:
# 		print("%s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset))

#directKafkastream.transform(storeOffsetRanges).foreachRDD(printOffsetRanges)
ssc.start()
ssc.awaitTermination()