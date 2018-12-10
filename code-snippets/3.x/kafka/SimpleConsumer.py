# 08 Nov 2018 | Kafka - Simple Consumer

from kafka import KafkaConsumer
consumer = KafkaConsumer('my_topic')
for msg in consumer:
    print(msg)

