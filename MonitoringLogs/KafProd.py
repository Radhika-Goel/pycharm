from kafka import KafkaProducer
from datetime import datetime
import time , json
from subprocess import PIPE,Popen,getoutput

KAFKA_TOPIC = 'agentMonitor'
KAFKA_BROKERS = ''


def generate_message():
    timestamp = int(datetime.now().strftime("%s"))
    hostname = getoutput("hostname")
    command = "ps -aef | grep kafka | grep -v grep | awk -F' ' 'END   {print $2}'"
    pid_value = getoutput(command)
    command = "ps -p %s -o pcpu= -o pmem=" % pid_value
    values=getoutput(command)
    message = '{"Hostname":"%s","recordTime":%s,"CPU":%s,"Mem":%s}'%(hostname,timestamp,values.split("  ")[1],values.split("  ")[2])
    print(message)
    return message


def publish_message(producer_instance ,topic_name,key,value):
    try:
        #key_bytes = bytes(key, encoding='utf-8')
        #value_bytes = bytes(value, encoding='utf-8')
        #record = json.loads(json.dumps(value))
        #print(type(record))
        #producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        #record = value
        producer_instance.send(topic_name, {key: value})
        #producer_instance.send(record)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def kafka_prodcuer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10),value_serializer=lambda m: json.dumps(m).encode('ascii'))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


if __name__ == '__main__':
    kafka_producer = kafka_prodcuer()
    while True:
        value = generate_message()
        #value='{152222: {"test": {"CPU": 0.4, "Mem": 0.1}}}'
        #print(value)
        publish_message(kafka_producer, 'agentMonitor', 'data', value)
        #publish_message(kafka_producer, 'agentMonitor',  value)
        time.sleep(60)
        #if kafka_producer is not None:
        #   kafka_producer().close('')
