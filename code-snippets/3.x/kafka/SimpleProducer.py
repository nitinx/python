# 08 Nov 2018 | Kafka - Simple Producer

from kafka import KafkaProducer
producer = KafkaProducer(bootstrapservers='localhost:1234')
for _ in range(100):
    producer.send('foobar', b'some_message_bytes')

