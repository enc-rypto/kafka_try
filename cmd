docker run -p 2181:2181 zookeeper
#to start zookeeper

docker run -p 9092:902\
-e KAFAKA_ZOOKEEPER_CONNECT = <IP>:2181\
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://<PRIVATE_IP>:9092 \
-e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
confluentinc/cp-kafka
