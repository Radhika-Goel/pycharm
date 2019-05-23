
import requests , json
from elasticsearch import Elasticsearch



es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

message='{"Hostname":"Radhikas-MacBook-Pro.local", "recordTime":1546740312,"CPU":0.3,"Mem":0.7}}'
print(json.loads(message))
es.index(index='monitor', doc_type='_doc',id = 1 , body=json.loads(message))






#client = MongoClient('localhost:27017')
#collection = client.numtest.numtest

#for message in consumer:
#	message = message.value
#	collection.insert_one(message)
#	print('{} added to {}'.format(message, collection))
