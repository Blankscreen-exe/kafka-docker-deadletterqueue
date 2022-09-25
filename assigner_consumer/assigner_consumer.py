#TODO: define a profile variable
consumer_serial = "consumer1"

# reading settings for this consumer
setting = json.loads(open(r"settings.json").read())

# imorting dependencies
from kafka import KafkaConsumer

# creating consumer object
consumer = KafkaConsumer(
    setting["consumerMetrics"][consumer_serial]["topics"][0], 
    group_id=setting["consumerMetrics"][consumer_serial]["groupID"]
    )

#TODO: consume from kafka stream
for item in consumer:
    print(item)


#TODO: send to related consumers for logging
