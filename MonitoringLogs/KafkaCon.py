from kafka import KafkaConsumer
import json
import requests , json , os
from elasticsearch import Elasticsearch

consumer = KafkaConsumer(
	'agentMonitor',auto_offset_reset='latest',bootstrap_servers=['localhost:9092'],
	enable_auto_commit=False,
	group_id='test-consumer-group')

es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])


i = 1
for message in consumer:
	print('Running Consumer..')
    #parsed_records = []
	#record = msg.value
	print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
										  message.offset, message.key,
										  message.value))
	#print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
	#									 message.offset,
	#									 message.value))
	#Values = record['Radhikas-MacBook-Pro.local']
	#recordTime = Values['recordTime']
	#print(record)
	#print(type(msg))
	#es.index(index='monitor', doc_type='test',body=json.loads(json.dumps(docket_content)))
	record = json.loads(message.value)
	newValue = record['data']
	print(newValue)
	#data = message.value.replace("\\", r"\\")
	#print(json.dumps(data))
	es.index(index='monitor', doc_type='_doc',id = i , body=json.loads(newValue))
	i = i + 1





#client = MongoClient('localhost:27017')
#collection = client.numtest.numtest

#for message in consumer:
#	message = message.value
#	collection.insert_one(message)
#	print('{} added to {}'.format(message, collection))
