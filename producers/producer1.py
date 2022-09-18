# configuration for this producer
producer_serial = "producer1"

#essential imports
from kafka import KafkaProducer
from time import sleep
import json
import path
import sys

# importing utility functions
directory = path.Path(__file__).abspath()
sys.path.append(directory.parent.parent)
from data_gen.data_gen import data_create
from data_validator import data_validate
#TODO: import status checker
from DeadLetterQueue.dlq_corrupt_producer import produce_to_corrupt_dlq

# reading settings for this producer
setting = json.loads(open(r"settings.json").read())

# creating a producer object for Kafka Queue
producer = KafkaProducer(
            bootstrap_servers=setting["kafkaSetup"]["brokerList"][0]
)

# data packet count variable
count = 0

# opening log file
logfilepath = f"logs/{producer_serial}_log.txt"
logFile = open(logfilepath, "a")

if __name__ == '__main__':

    while True:
        # generate data
        data = data_validate(data_create(
            count,
            setting["producerMetrics"][producer_serial]["targetId"],
            setting["producerMetrics"][producer_serial]["id"],
            setting["dataGeneratorSettings"]["errFrequency"]))

        # create log
        log = f'''
        ProducerID: {setting["producerMetrics"][producer_serial]["id"]}
        Message Serial: {count}
        Data Sent >> {data}
        '''
        print(log)

        # append log to file
        logFile.write(log)

        # send data
        try:
            if "playerErr" in data.keys() or "countryErr" in data.keys() or "teamErr" in data.keys():
                AnomalyReport = f"""
                !!! Anomalies Found !!!
                locations:
                PlayerName: {data["playerErr"]}
                CountryName: {data["countryErr"]}
                TeamName: {data["teamErr"]}
                """
                print(AnomalyReport)
                raise ValueError
        except:
            sendingInfo = "sending data to DLQ ...\n===== Generating next data packet ====="
            logFile.write(sendingInfo)
            print(sendingInfo)

            #TODO: send to DLQ 
            produce_to_corrupt_dlq(data)
        else:
            sendingInfo = "sending data to Queue ...\n===== Generating next data packet ====="
            logFile.write(sendingInfo)
            print(sendingInfo)

            #TODO: send to demux producer
            #TODO: if demux producer return "true" then send data to "no space dlq"
            producer.send(
                setting["producerMetrics"][producer_serial]["topics"][0],
                data
                )

        # wait for certain time period
        if not setting["producerMetrics"][producer_serial]["timeSleepDisable"]:
            sleep(setting["producerMetrics"][producer_serial]["timeInterval"])

        # count increment
        count += 1
