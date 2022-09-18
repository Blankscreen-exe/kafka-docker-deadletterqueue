import json
from kafka import KafkaProducer

# reading settings for this producer
setting = json.loads(open(r"settings.json").read())

# creating a producer object for Dead Letter Queue
producer = KafkaProducer(
            bootstrap_servers=setting["DLQSetup"]["brokerList"][0]
)

def produce_to_corrupt_dlq(data):

    producer.send(
                setting["DLQMetrics"]["corruptDLQ"]["topics"][0],
                data
                )
