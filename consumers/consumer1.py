#TODO: define a profile variable
consumer_serial = "consumer1"

# reading settings for this consumer
setting = json.loads(open(r"settings.json").read())

# imorting dependencies
from kafka import KafkaConsumer

# creating consumer object
consumer = KafkaConsumer(setting["consumerMetrics"][consumer_serial]["topics"][0])

#TODO: create a function which takes in data and creates a log in "logs" folder
#also prints to stdout
