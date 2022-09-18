
import json

# reading settings for this producer
setting = json.loads(open(r"settings.json").read())


def statusChecker (topic, brokerServer):
    #TODO: check status of queue if its filled or not
    #TODO: send data to "no space dlq" if filled==True
    pass

messageCounter = [0]*setting["demuxProducer"]["numberOfQueues"]

def messageCounter():
    #TODO: make a counter that keeps track of sent messages for each queue.
    messageCounter[0] += 1

