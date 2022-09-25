# Kafka DeadLetter Exchange/Delay Mechanism

## Introduction
This mechanism is introduced as a solution to data being rejected or dropped before being produced to a `Kafka-Broker Topic`.
We also consider the possibilities that a `Kafka Broker` sends a data packet but that data is not recieved by a `consumer`.
This mechanism simply resolved that issue and established a `Dead Letter Queue` as a reliable queue which will not only host a sequence of dead-letters but also the corrupted data which should be allowed to enter into a `Kafka Queue`.

## References
1- Error Handling via Dead Letter Queue in Apache Kafka (source: [kai-waehner.de](https://www.kai-waehner.de/blog/2022/05/30/error-handling-via-dead-letter-queue-in-apache-kafka/))