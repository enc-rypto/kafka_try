# Import KafkaProducer from Kafka library
from kafka import KafkaProducer

import time

# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name where the message will publish
topicName = 'First_Topic'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Publish text in defined topic
for i in range(100):
    producer.send(topicName, b'Hii everyone from kafka')
    time.sleep(1)

# Print message
print("Message Sent")
