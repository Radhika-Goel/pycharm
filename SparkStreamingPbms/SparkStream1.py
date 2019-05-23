import sys
from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from uuid import uuid1
import json

if __name__ == __main__:
	sc = SparkContext(appName = 'testSparkStreaming')
	ssc = StreamingContext(sc,2) #Batch Interval

	broker,topic = sys.argv[1:]
	kvs = KafkaUtils.createStream(ssc,broker,"raw-event-streaming-consumer",{topic:1})
	lines = kvs.map(lambda x: json.loads(x[1]))
	counts = lines.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)) .reduceByKey(lambda a, b: a+b)

	# Count number of tweets in the batch
	count_this_batch = kvs.count().map(lambda x:('Tweets this batch: %s' % x))

	# Count by windowed time period
	count_windowed = kvs.countByWindow(60,5).map(lambda x:('Tweets total (One minute rolling count): %s' % x))

	## --- Processing
	# Extract tweets
	parsed = kvs.map(lambda v: json.loads(v[1]))
#Get authors
	authors_dstream = parsed.map(lambda tweet: tweet['user']['screen_name'])

	counts.pprint()
	ssc = StreamingContext.getOrCreate('/tmp/checkpoint_v01',lambda: createContext()) #CreateContext is the class Nmae
	ssc.start()
	ssc.awaitTermination()



#$ bin/spark-submit — packages org.apache.spark:spark-streaming-kafka-0–8_2.11:2.0.0 spark-direct-kafka.py localhost:9092 new_topic